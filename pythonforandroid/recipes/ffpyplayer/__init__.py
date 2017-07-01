from pythonforandroid.toolchain import Recipe, CythonRecipe, shprint, current_directory, ArchARM
from os.path import exists, join, realpath
from os import uname
import glob
import sh
import os


class FFPyPlayerRecipe(CythonRecipe):
    version = 'android_sdl_mixer'
    url = 'https://github.com/rammie/ffpyplayer/archive/{version}.zip'
    depends = ['python2', 'sdl2', 'sdl2_mixer', 'ffmpeg']
    opt_depends = ['openssl', 'ffpyplayer_codecs']

    def get_recipe_env(self, arch, with_flags_in_cc=True):
        env = super(FFPyPlayerRecipe, self).get_recipe_env(arch)

        env["USE_SDL2_MIXER"] = "1"
        env["SDL_MIXER_INCLUDE_DIR"] = join(self.ctx.bootstrap.build_dir, 'jni', 'SDL2_mixer')
        env["SDL_INCLUDE_DIR"] = join(self.ctx.bootstrap.build_dir, 'jni', 'SDL', 'include')
        env["SDL_LIB_DIR"] = join(self.ctx.bootstrap.build_dir, 'libs', arch.arch)

        build_dir = Recipe.get_recipe('ffmpeg', self.ctx).get_build_dir(arch.arch)
        env["FFMPEG_INCLUDE_DIR"] = join(build_dir, "include")
        env["FFMPEG_LIB_DIR"] = join(build_dir, "lib")

        return env

recipe = FFPyPlayerRecipe()
