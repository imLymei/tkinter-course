import customtkinter as ctk
from PIL import Image
from os import walk

class AnimatedButton(ctk.CTkButton):
    def __init__(self, parent, light_path, dark_path):
        self.frames = self.import_folders(light_path, dark_path)
        self.frame_index = 0
        self.animation_length = len(self.frames)-1
        self.animation_status = ctk.StringVar(value='start')
        self.on_loop = False

        self.animation_status.trace('w', self.animate_loop)

        super().__init__(master=parent, text='Animated Button',
                         image=self.frames[self.frame_index],
                         command=self.trigger_animation)
        self.pack(expand=True)

    def import_folders(self, light_path, dark_path):
        image_paths = []
        for path in (light_path, dark_path):
            for _, __, data in walk(path):
                sorted_data = sorted(data, key=lambda item: int(item.split('.')[0][-5:]))
                full_path_data = [path + '/' + item for item in sorted_data]
                image_paths.append(full_path_data)
        image_paths = zip(*image_paths)

        ctk_images = []
        for image_path in image_paths:
            ctk_image = ctk.CTkImage(light_image=Image.open(image_path[0]),
                                     dark_image=Image.open(image_path[1]))
            ctk_images.append(ctk_image)

        return ctk_images

    def trigger_animation(self):
        self.on_loop = not self.on_loop
        print(self.on_loop)
        if self.animation_status.get() == 'start':
            self.frame_index = 0
            self.animation_status.set('forward')
        elif self.animation_status.get() == 'end':
            self.frame_index = self.animation_length
            self.animation_status.set('backward')
        else:
            temp = self.animation_status.get()
            self.animation_status.set('a')
            self.animation_status.set(temp)


    def animate(self, *agrs):
        if self.animation_status.get() == 'forward':
            self.frame_index += 1
            self.configure(image=self.frames[self.frame_index])
            if self.frame_index < self.animation_length:
                self.after(20, self.animate)
            else:
                self.animation_status.set('end')
        elif self.animation_status.get() == 'backward':
            self.frame_index -= 1
            self.configure(image=self.frames[self.frame_index])
            if self.frame_index > 0:
                self.after(20, self.animate)
            else:
                self.animation_status.set('start')

    def animate_loop(self, *agrs):
        if self.on_loop:
            if self.animation_status.get() == 'forward':
                self.frame_index += 1
                self.configure(image=self.frames[self.frame_index])
                if self.frame_index < self.animation_length:
                    self.after(20, self.animate_loop)
                else:
                    self.animation_status.set('backward')
            elif self.animation_status.get() == 'backward':
                self.frame_index -= 1
                self.configure(image=self.frames[self.frame_index])
                if self.frame_index > 0:
                    self.after(20, self.animate_loop)
                else:
                    self.animation_status.set('forward')


window = ctk.CTk()
window.title('Animations')
window.geometry('300x200')

AnimatedButton(window, '../src/animations/light', '../src/animations/dark')

window.mainloop()
