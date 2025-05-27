from stylegan2_pytorch import Trainer

trainer = Trainer(
    data='./data/faces',  # Replace with the folder path of your training images
    results_dir='./results',
    models_dir='./models',
    image_size=128,
    network_capacity=16,
    batch_size=4
)

print("Everything is working. Ready to train.")
