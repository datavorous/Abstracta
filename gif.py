from PIL import Image

def create_gif(image_path, output_path,duration=200):
	images = [Image.open(image_path) for image_path in image_paths] 

	images[0].save(
		output_path,
		save_all=True,
		append_images=images[1:],
		duration=duration,
		loop=0
		)


image_paths = []

for a in range(20,600,20):
	image_paths.append(f"bluejay/progress_{a}.png")

output_path = "output.gif"
print(image_paths)
create_gif(image_paths, output_path)