# This function should take in an RGB image and return a new, standardized version
def standardize_input(image, crop=8):
    ## TODO: Resize image and pre-process so that all "standard" images are the same size
    standard_im = np.copy(image)
    cropped_image = standard_im[crop:-crop, crop:-crop, :]
    resized_image = cv2.resize(cropped_image, (32, 32))
    return resized_image


## TODO: One hot encode an image label
## Given a label - "red", "green", or "yellow" - return a one-hot encoded label

# Examples:
# one_hot_encode("red") should return: [1, 0, 0]
# one_hot_encode("yellow") should return: [0, 1, 0]
# one_hot_encode("green") should return: [0, 0, 1]

def one_hot_encode(label):
    ## TODO: Create a one-hot encoded label that works for all classes of
    # traffic lights
    one_hot_encoded = [0, 0, 0]

    if label == 'red':
        one_hot_encoded[0] = 1
    elif label == 'yellow':
        one_hot_encoded[1] = 1
    else:
        one_hot_encoded[2] = 1

    return one_hot_encoded


## TODO: Create a brightness feature that takes in an RGB image and outputs a feature vector and/or value
## This feature should use HSV colorspace values


def display_plot(rgb_image, masked_image):
    """Displays a pyplot of rgb_image and masked_image."""
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
    ax1.set_title('rgb')
    ax1.imshow(rgb_image, cmap='gray')
    ax2.set_title('hsv')
    ax2.imshow(masked_image, cmap='gray')


def is_red(features):
    """Helps determine if image is a red light via it's hue feature."""
    hue, saturation, value = features
    if sum(saturation[0:10]) < sum(hue[0:10]):
        return False
    return True


def create_masked_image(rgb_image, lower_limit, upper_limit):
    """Creates a masked image given an rgb_image, and the lower and upper limits."""
    mask = cv2.inRange(rgb_image, lower_limit, upper_limit)
    masked_image = np.copy(rgb_image)
    masked_image[mask != 0] = [0, 0, 0]
    return masked_image


def create_feature(rgb_image):
    """Brightness feature that takes an rgb_image and returns its HSV vector."""
    # Create mask
    lower_gray = np.array([0, 0, 0])
    upper_gray = np.array([50, 50, 50])  # 50 is best
    masked_image = create_masked_image(rgb_image, lower_gray, upper_gray)

    ## TODO: Convert image to HSV color space
    hsv_image = cv2.cvtColor(masked_image, cv2.COLOR_RGB2HSV)

    # Get and sum features
    hue = hsv_image[:, :, 0]
    saturation = hsv_image[:, :, 1]
    value = hsv_image[:, :, 2]

    hue_sum = np.sum(hue[:, :], axis=1)
    saturation_sum = np.sum(saturation[:, :], axis=1)
    value_sum = np.sum(value[:, :], axis=1)

    ## TODO: Create and return a feature value and/or vector
    features = [hue_sum, saturation_sum, value_sum]

    # Helps to determine if a light is red
    features[0] = np.array([0] * len(hue_sum))

    # display_plot(rgb_image, masked_image)  # for testing purposes

    return features


# (Optional) Add more image analysis and create more features


def create_bw_feature(rgb_image):
    """Brightness feature that takes an rgb_image and returns its HSV vector."""
    # Create mask
    lower_gray = np.array([0, 0, 0])
    upper_gray = np.array([50, 50, 50])  # 50 is best
    masked_image = create_masked_image(rgb_image, lower_gray, upper_gray)

    # Get and sum features
    bw_image = cv2.cvtColor(masked_image, cv2.COLOR_RGB2GRAY)
    brightness = np.sum(bw_image[:, :], axis=1)
    # display_plot(rgb_image, bw_image)  # for testing purposes

    return brightness


create_bw_feature(test_im)


# This function should take in RGB image input
# Analyze that image using your feature creation code and output a one-hot
# encoded label
def estimate_label(rgb_image):
    ## TODO: Extract feature(s) from the RGB image and use those features to
    ## classify the image and output a one-hot encoded label
    predicted_label = [0, 0, 0]

    hue, saturation, value = create_feature(rgb_image)
    brightness = create_bw_feature(rgb_image)

    hsv_brightness = [x + y + z for x, y, z in zip(hue, saturation, value)]
    bw_brightness = [x + y for x, y in zip(hsv_brightness, brightness)]
    total_brightness = [x + y for x, y in zip(hsv_brightness, bw_brightness)]

    max_brightness = total_brightness.index(max(total_brightness))

    if max_brightness in range(0, 11):
        predicted_label[0] = 1
    elif max_brightness in range(10, 21):
        predicted_label[1] = 1
    else:
        predicted_label[2] = 1

    return predicted_label


estimate_label(test_im)