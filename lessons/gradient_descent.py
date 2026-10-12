"""TinyMind-001: learn linear regression with gradient descent.

Run locally or in Google Colab. Uses only Python's standard library.
Try LEARNING_RATE = 0.001, 0.01, and 0.1, then compare the loss.
"""

X_DATA = [1, 2, 3, 4, 5]
Y_DATA = [3, 5, 7, 9, 11]

LEARNING_RATE = 0.01
EPOCHS = 1000


def train(learning_rate=LEARNING_RATE, epochs=EPOCHS):
    w = 0.0
    b = 0.0
    n = len(X_DATA)

    for epoch in range(epochs):
        dw = 0.0
        db = 0.0
        loss = 0.0

        for x, y in zip(X_DATA, Y_DATA):
            prediction = w * x + b
            error = prediction - y
            loss += error ** 2
            dw += 2 * error * x / n
            db += 2 * error / n

        # Move parameters against the gradient to reduce loss.
        w -= learning_rate * dw
        b -= learning_rate * db

        if epoch % 200 == 0:
            print(
                f"epoch={epoch:4d} | loss={loss / n:.6f} "
                f"| w={w:.4f} | b={b:.4f}"
            )

    final_loss = sum((w * x + b - y) ** 2 for x, y in zip(X_DATA, Y_DATA)) / n
    print("\nTraining finished")
    print(f"learning rate: {learning_rate}")
    print(f"w = {w:.4f} (target: 2)")
    print(f"b = {b:.4f} (target: 1)")
    print(f"final mean squared error = {final_loss:.6f}")
    test_x = 6
    print(f"x={test_x}, prediction={w * test_x + b:.4f} (target: 13)")
    return w, b, final_loss


if __name__ == "__main__":
    train()
