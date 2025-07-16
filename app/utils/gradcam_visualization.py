#!/usr/bin/env python
# coding: utf-8

# In[3]:


def histo_GradCAM(best_model,tissue_image_array,true_class=None):

    tissue_types=['ADI','DEB','LYM','MUC','MUS','NOR','STR','TUM']
    tissue_label_dict= {}
    
    for i,tissue in enumerate(tissue_types):
        tissue_label_dict.update({i:tissue}) 

    tissue_image_array= np.expand_dims(tissue_image_array, axis=0) # keras models expect batches of images, even if it's just one image.
    tissue_gradcam_model= tf.keras.models.Model(best_model.inputs,[best_model.get_layer("top_conv").output, best_model.output])
    
    with tf.GradientTape() as tape:
        lastconv_output,preds = tissue_gradcam_model(tissue_image_array)
        pred_class= tf.argmax(preds[0])
        pred_prob=preds[:,pred_class]
    
    grads= tape.gradient(pred_prob,lastconv_output)
    
    grads= grads[0]
    lastconv_output=lastconv_output[0]
    
    pooled_grads=tf.reduce_mean(grads, axis=(0, 1))
    weighted_output=lastconv_output * pooled_grads
    heatmap=tf.reduce_sum(weighted_output,axis=2)

    heatmap_resized= tf.image.resize(heatmap[..., tf.newaxis], size=(224, 224))
    heatmap_resized= tf.squeeze(heatmap_resized).numpy()
    heatmap_resized= (heatmap_resized- np.min(heatmap_resized))/(np.max(heatmap_resized)-np.min(heatmap_resized)+1e-8)
    colormap= mpl.colormaps['jet']
    heatmap_rgb= colormap(np.uint8(255 * heatmap_resized))[:, :, :3]
    heatmap_rgb= np.uint8(heatmap_rgb * 255)

    
    tissue_image_array= tf.squeeze(tissue_image_array).numpy()
    
    alpha= 0.6
    overlay= np.uint8(heatmap_rgb * alpha + tissue_image_array * (1 - alpha))
    fig,ax= plt.subplots(1, 2, figsize=(10, 5))

    # Tissue image from the dataset
    ax[0].imshow(tissue_image_array.astype('uint8'))
    ax[0].axis('off')
    ax[0].set_title(f"Histological Image\n(True: {true_class})" if true_class else "Histological Image")
    
    # With Grad-CAM overlay showing model's prediction
    ax[1].imshow(overlay.astype('uint8'))
    ax[1].axis('off')
    ax[1].set_title(f"Regions Influencing Prediction (Grad-CAM)\n"
                     f"(Pred:{tissue_label_dict[pred_class.numpy()]} | Prob:{pred_prob.numpy()[0]:.2f})")

    
    plt.tight_layout()
    plt.show()
    
    return {'original': tissue_image_array.astype('uint8'),
            'heatmap':heatmap_resized,'overlay': overlay,
            'true_class':true_class,
            'pred_class':tissue_label_dict[pred_class.numpy()],
            'pred_prob':pred_prob.numpy()[0]}
    
        
    


# In[ ]:




