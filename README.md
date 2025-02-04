# RapidBase

RapidBase is a lightweight Python application that allows users to quickly adjust display settings such as brightness and contrast directly from the system tray on Windows.

## Features

- Adjust screen brightness from 0% to 100% in increments of 10%.
- Placeholder feature for adjusting contrast (actual implementation may vary).
- Easy access from the system tray.
- Simple and intuitive interface.

## Requirements

- Python 3.x
- PyQt5
- screen_brightness_control

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/rapidbase.git
    cd rapidbase
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create an icon named `icon.png` to represent the application in the system tray.

## Usage

To run the application, execute the following command:
```bash
python rapidbase.py
```

Once the application is running, you will find an icon in the system tray. Right-click the icon to access brightness and contrast settings.

## Notes

- The brightness adjustment is implemented using the `screen_brightness_control` library. Ensure that your system is compatible with this library.
- The contrast adjustment is currently a placeholder. The implementation for adjusting contrast may require additional libraries or system-specific code.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

```

This setup should give you a basic application to adjust screen brightness and a placeholder for contrast adjustments. Note that the contrast functionality is not implemented due to system-specific requirements and limitations in Python libraries, and it's currently a placeholder.