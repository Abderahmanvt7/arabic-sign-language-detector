![Banner](./logo.png)

# Arabic Sign Language Detector

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0F9D58.svg?style=for-the-badge&logo=MediaPipe&logoColor=white)](https://mediapipe.dev/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

## Project Overview

The Arabic Sign Language Detector is an innovative computer vision project that uses machine learning to recognize and interpret Arabic sign language in real-time. This system can detect individual Arabic sign language characters, providing a foundation for more complex sign language interpretation.

## Features

- Real-time detection of Arabic sign language characters
- Uses computer vision and machine learning techniques
- Custom dataset creation tools
- High accuracy in character recognition (99.66% on test set)

## Installation

### Requirements

Before installing the project, ensure you have Python installed on your system. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

### Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/Abderahmanvt7/arabic-sign-language-detector.git
   cd arabic-sign-language-detector
   ```

2. Install the required dependencies as mentioned above.

3. Download the Arabic font file "NotoSansArabic-VariableFont_wdth,wght.ttf" and place it in a `fonts` folder in the project directory.

## Usage

The project consists of four main scripts:

1. **Data Collection**: Run `collect_imgs.py` to capture images for the dataset:

   ```bash
   python collect_imgs.py
   ```

   This script will guide you through the process of capturing images for each sign.

2. **Dataset Creation**: Process the captured images to create the dataset:

   ```bash
   python create_dataset.py
   ```

3. **Model Training**: Train the classifier on the processed dataset:

   ```bash
   python train_classifier.py
   ```

4. **Real-time Detection**: Use the trained model for real-time sign language detection:
   ```bash
   python inference_classifier.py
   ```

## Model Performance

The current model achieves an accuracy of 99.66% on the test set, demonstrating high reliability in recognizing individual Arabic sign language characters.

## Limitations and Future Work

- Currently, the system can only recognize individual characters.
- Future improvements aim to enable the recognition of words and sentences.
- Expanding the dataset to include more varied samples could further improve accuracy and robustness.

## Contributing

Contributions to improve the Arabic Sign Language Detector are welcome. Please feel free to submit pull requests or open issues to discuss potential enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any problems or have suggestions:

1. Check the [Issues](https://github.com/Abderahmanvt7/arabic-sign-language-detector/issues) page
2. Create a new issue if needed
3. Contact the maintainers

---

This project is part of an ongoing effort to make technology more accessible and to bridge communication gaps. We hope it serves as a stepping stone towards more comprehensive sign language interpretation systems.

---

Made with ❤️ by [Abderahman HAMILI](https://github.com/Abderahmanvt7)
