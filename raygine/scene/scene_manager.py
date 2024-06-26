from typing import Self
from .scene import Scene


class SceneManager:
    def __init__(self) -> None:
        self.scenes: dict[str, Scene] = {
            'default': Scene()
        }
        self.current_scene: str = None
        self.change_scene('default')
    
    def add_scene(self, scene: Scene, name: str) -> Self:
        self.scenes[name] = scene
        return self
    
    def remove_scene(self, name: str) -> Self:
        if name == "default": 
            print("Can't delete default scene, its there as a fallback")
            return
        if name in self.scenes:
            if self.current_scene == name: 
                self.change_scene("default")
            del self.scenes[name]
        return self
    
    def get_scene(self, name: str) -> Scene | None:
        return self.scenes.get(name)
    
    def get_current_scene(self) -> Scene:
        if self.current_scene not in self.scenes:
            self.change_scene("default")
        return self.get_scene(self.current_scene)
    
    def change_scene(self, name: str, *args, **kwargs) -> None:
        unload_ret = None
        if not self.current_scene is None:
            unload_ret = self.get_current_scene().unload()
        self.current_scene = name
        self.get_current_scene().load(*args, **kwargs)
        return unload_ret
    
    def update_scene(self) -> None:
        self.get_current_scene().update()
        # self.get_current_scene().render()
    
    def render_scene(self) -> None:
        self.get_current_scene().render()
    
    
