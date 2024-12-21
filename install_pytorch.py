import subprocess
import sys
import platform
import os

def get_cuda_version():
    """Check if CUDA is available and get its version"""
    try:
        nvcc_output = subprocess.check_output(['nvcc', '--version']).decode('utf-8')
        # Extract CUDA version from nvcc output
        cuda_version = next(line for line in nvcc_output.split('\n') if 'release' in line)
        return cuda_version
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

def install_pytorch():
    """Install PyTorch with appropriate configuration"""
    print("Starting PyTorch installation process...")
    
    # Check Python version
    python_version = sys.version_info
    print(f"Detected Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # Check operating system
    os_name = platform.system()
    print(f"Detected OS: {os_name}")
    
    # Check CUDA availability
    cuda_version = get_cuda_version()
    if cuda_version:
        print(f"CUDA detected: {cuda_version}")
        install_command = [
            sys.executable,
            "-m",
            "pip",
            "install",
            "torch",
            "torchvision",
            "torchaudio",
            "--index-url",
            "https://download.pytorch.org/whl/cu118"  # Using CUDA 11.8 as it's stable
        ]
    else:
        print("No CUDA detected, installing CPU-only version")
        install_command = [
            sys.executable,
            "-m",
            "pip",
            "install",
            "torch",
            "torchvision",
            "torchaudio",
            "--index-url",
            "https://download.pytorch.org/whl/cpu"
        ]
    
    print("\nInstalling PyTorch...")
    print("This may take a few minutes...")
    
    try:
        subprocess.check_call(install_command)
        print("\nPyTorch installation completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"\nError installing PyTorch: {str(e)}")
        return False
    
    # Verify installation
    try:
        import torch
        print(f"\nPyTorch version: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")
        return True
    except ImportError:
        print("\nPyTorch installation verification failed!")
        return False

def install_dependencies():
    """Install other required dependencies"""
    dependencies = [
        "transformers>=4.30.0",
        "peft>=0.8.2",
        "datasets>=2.16.1",
        "accelerate>=0.20.0"
    ]
    
    print("\nInstalling additional dependencies...")
    
    for dep in dependencies:
        try:
            print(f"Installing {dep}")
            subprocess.check_call([
                sys.executable,
                "-m",
                "pip",
                "install",
                dep
            ])
        except subprocess.CalledProcessError as e:
            print(f"Error installing {dep}: {str(e)}")
            return False
    
    return True

def main():
    print("=== PyTorch Installation Script for Python 3.12 ===\n")
    
    # Install PyTorch
    if not install_pytorch():
        print("\nPyTorch installation failed. Please check the error messages above.")
        return
    
    # Install dependencies
    if not install_dependencies():
        print("\nDependency installation failed. Please check the error messages above.")
        return
    
    print("\n=== Installation Complete ===")
    print("\nYou can now run the following test code to verify everything works:")
    print("""
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Verify PyTorch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")

# Test model loading
model_name = "bigscience/bloomz-560m"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True
)
    """)

if __name__ == "__main__":
    main()