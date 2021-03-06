# in this model, images are only resized directly
# using cifar-10 model structure

from conf import *
import data_reader as data_reader

NB_EPOCHS = 200

train_csv, test_csv = data_reader.load_csv()

# change data augmentation methods here
images = data_reader.load_image_data_resize_directly()
# load train labels (one-hot encoding)
train_labels_orig = data_reader.load_train_labels()

# separate train and test from images
train_images_orig = np.expand_dims(np.array([images[str(idx)] for idx in train_csv.id]), axis=4)
test_images = np.expand_dims(np.array([images[str(idx)] for idx in test_csv.id]), axis=4)
print(train_images_orig.shape)
print(test_images.shape)

# split original train into train and validation
nb_train = int(len(train_images_orig) * 0.9)
nb_val = len(train_images_orig) - nb_train
train_indices = random.sample(range(0, len(train_images_orig)), nb_train)
val_indices = [x for x in range(0, len(train_images_orig)) if x not in train_indices]

train_images = train_images_orig[train_indices, :, :, :]
train_labels = train_labels_orig[train_indices, :]
val_images = train_images_orig[val_indices, :, :, :]
val_labels = train_labels_orig[val_indices, :]

print('train_images shape', train_images.shape)
print('val_images shape', val_images.shape)

imgen = ImageDataGenerator(
    featurewise_center=True,
    featurewise_std_normalization=True,
    zca_whitening=True,
    rotation_range=90,
    zoom_range=0.2,
    fill_mode='nearest',
    horizontal_flip=True,
    vertical_flip=True)
imgen.fit(train_images)
imgen_flow = imgen.flow(train_images, train_labels, batch_size=16)

img_model = Sequential()

img_model.add(Conv2D(32, (3, 3), padding='same', input_shape=train_images.shape[1:]))
img_model.add(Activation('relu'))
img_model.add(Conv2D(32, (3, 3), padding='same'))
img_model.add(Activation('relu'))
img_model.add(MaxPooling2D(pool_size=(2, 2)))
img_model.add(Dropout(0.25))

img_model.add(Conv2D(64, (3, 3), padding='same'))
img_model.add(Activation('relu'))
img_model.add(Conv2D(64, (3, 3), padding='same'))
img_model.add(Activation('relu'))
img_model.add(MaxPooling2D(pool_size=(2, 2)))
img_model.add(Dropout(0.25))

img_model.add(Flatten())
img_model.add(Dense(512))
img_model.add(Activation('relu'))
img_model.add(Dropout(0.5))
img_model.add(Dense(99))
img_model.add(Activation('softmax'))

opt = keras.optimizers.adam(lr=0.0001, decay=1e-6)
img_model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

img_model.count_params()
img_model.summary()

img_history = img_model.fit_generator(imgen_flow,
                                      epochs=200,
                                      validation_data=(val_images, val_labels),
                                      steps_per_epoch=len(train_images)/16)

# plt.plot(img_history.history['acc'])
# plt.xlabel('Iterations')
# plt.ylabel('Training Accuracy')
# plt.title('Training Accuracy')
# plt.show()

# plt.plot(img_history.history['val_acc'])
# plt.xlabel('Iterations')
# plt.ylabel('Validation Accuracy')
# plt.title('Validation Accuracy')
# plt.show()

# plt.plot(img_history.history['acc'])
# plt.plot(img_history.history['val_acc'])
# plt.xlabel('Iterations')
# plt.ylabel('Accuracy')
# plt.title('Training and Validation Accuracy')
# plt.legend(['train', 'validation'], loc='upper left')
# plt.show()

fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.plot(img_history.history['acc'])
ax.plot(img_history.history['val_acc'])
plt.xlabel('Iterations')
plt.ylabel('Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend(['train', 'validation'], loc='upper left')
fig.savefig('accuracy.png')   # save the figure to file
plt.close(fig)