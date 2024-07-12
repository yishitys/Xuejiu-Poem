# A Simple Approach of Chinese Poetry Generation Using Pre-trained LLM

## Overview
This project is based on a research paper and aims to generate ancient Chinese poems using pre-trained language models (LLMs). Leveraging the power of advanced neural networks, the project provides a straightforward approach to creating poetic compositions in Chinese.

## Features
- **Pre-trained LLM Integration**: Utilizes state-of-the-art pre-trained language models for generating poetry.
- **User-Friendly Interface**: Simple and intuitive interface for users to interact with the poetry generation tool.
- **Customizable Parameters**: Allows users to adjust parameters for more tailored poetic outputs.
- **Rich Dataset**: Built upon a rich corpus of ancient Chinese poetry for training and fine-tuning the model.

## Models
We mainly trained the following models:
- [**Qwen1.5-1.8B-Chat**](https://huggingface.co/Qwen/Qwen1.5-14B-Chat)
- [**Qwen1.5-14B-Chat**](https://huggingface.co/Qwen/Qwen1.5-14B-Chat)

(Training based on [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory))

## Installation
To install and run the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/chinese-poetry-generation.git
    cd chinese-poetry-generation
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download pre-trained models**:
    - Provide the link or instructions to download the pre-trained models.

4. **Run the application**:
    ```bash
    python main.py
    ```

## Usage
Here are some examples of how to use the poetry generation tool:

1. **Generate a simple poem**:
    ```bash
    python generate_poem.py --length 4
    ```

2. **Customize the style and theme**:
    ```bash
    python generate_poem.py --length 4 --theme nature
    ```

## Contributing
We welcome contributions! If you'd like to contribute, please fork the repository and create a pull request. Here are some ways you can contribute:
- Report bugs
- Suggest features
- Submit pull requests for improvements

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Authors
- Zhengchen Li
- Jiuqiao Yu
- Yishi Tang
- Legend Yang

## Acknowledgements
- Special thanks to the developers of the pre-trained models used in this project.
- Inspired by the rich tradition of Chinese poetry and modern advancements in natural language processing.
