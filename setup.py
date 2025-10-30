from setuptools import setup, find_packages
from setuptools.command.install import install as _install
import subprocess
import os

REQUIRED_PIP_PACKAGES = [
    'gradio==3.16.2',
    'albumentations==1.3.0',
    'opencv-python>=4.5.5.62',
    'imageio==2.9.0',
    'imageio-ffmpeg==0.4.2',
    'omegaconf==2.1.1',
    'test-tube>=0.7.5',
    'streamlit==1.12.1',
    'einops==0.3.0',
    'transformers>=4.19.2',
    'invisible-watermark>=0.1.5',
    'streamlit-drawable-canvas==0.8.0',
    'addict==2.4.0',
    'yapf==0.32.0',
    'prettytable==3.6.0',
    'safetensors>=0.2.7',
    'fvcore',
    'pycocotools',
    'wandb',
    'scipy',
    'matplotlib',
    'pytorch-lightning>=2.0.0',  
    'torchmetrics>=1.0.0',     
    'kornia>=0.7.0',            
    'timm>=0.9.0',              
    'open_clip_torch>=2.2.0',   
    'webdataset',               
    'basicsr',                  
]

MIM_PACKAGES = [
    "mmengine",
    "mmcv>=2.0.1",
    "mmdet>=3.1.0",
    "mmpose>=1.1.0",
]

class CustomInstallCommand(_install):
    def run(self):
        _install.run(self)
        
        print("="*50)
        print("MIM Start")
        print("="*50)


        try:
            subprocess.check_call(['pip', 'install', '-U', 'openmim'])
        except subprocess.CalledProcessError as e:
            print(f"Fail for install openmim: {e}")
            return 
        
        mim_command = ['mim', 'install'] + MIM_PACKAGES
        
        try:
            subprocess.check_call(mim_command)
            print("MIM finish.")
        except subprocess.CalledProcessError as e:
            print(f"Fial for MIM installing。 {e}")
            return
        
        print("="*50)
        print("ExternalLib finish。")
        print("="*50)


setup(
    name='ExternalLib',
    version='0.1.0',
    packages=find_packages(),
    
    cmdclass={
        'install': CustomInstallCommand,
    },
    
    install_requires=REQUIRED_PIP_PACKAGES,

)