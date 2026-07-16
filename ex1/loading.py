import importlib


def check_dependencies():
    dependencies = {
        "numpy": "np",
        "pandas": "pd",
        "matplotlib.pyplot": "plt"
    }

    modules = {}

    for dependency, alias in dependencies.items():
        try:
            modules[alias] = importlib.import_module(dependency)
            print(f"[OK] {dependency} est installé")
        except ImportError:
            print(f"[ERROR] {dependency} n'est pas installé")
    if len(modules) == 0:
        modules = None
    return modules


def main():
    modules = check_dependencies()

    if modules is None:
        print("\nVeuillez installer les modules manquants en lancant :\n")
        print("pip install -r requirements")
        print("or : poetry install ")
        return

    np = modules["np"]
    pd = modules["pd"]
    plt = modules["plt"]

    np.random.seed(42)
    class_0 = np.random.randn(50, 2) + np.array([2, 2])
    class_1 = np.random.randn(50, 2) + np.array([6, 6])

    X = np.vstack((class_0, class_1))

    y = np.array(
        [0] * 50 + [1] * 50
    )

    data = pd.DataFrame(
        X,
        columns=["feature_1", "feature_2"]
    )

    data["label"] = y
    print("\nDataset :")
    print(data.head())
    indices = np.arange(len(X))
    np.random.shuffle(indices)

    learn_rate = 0.8

    split_index = int(len(X) * learn_rate)

    train_indices = indices[:split_index]
    test_indices = indices[split_index:]

    X_train = X[train_indices]
    y_train = y[train_indices]

    X_test = X[test_indices]
    y_test = y[test_indices]

    weights = np.zeros(X_train.shape[1])
    bias = 0.0

    learning_rate = 0.1
    epochs = 100

    errors_history = []
    for epoch in range(epochs):

        total_errors = 0

        for x, expected in zip(X_train, y_train):

            value = np.dot(x, weights) + bias

            if value >= 0:
                prediction = 1
            else:
                prediction = 0

            error = expected - prediction

            if error != 0:
                weights += learning_rate * error * x
                bias += learning_rate * error
                total_errors += 1

        errors_history.append(total_errors)

        print(
            f"Epoch {epoch + 1}/{epochs} "
            f"- Errors: {total_errors}"
        )

        if total_errors == 0:
            print("Training completed.")
            break

    values = np.dot(X_test, weights) + bias

    predictions = (values >= 0).astype(int)

    correct = np.sum(predictions == y_test)

    total = len(y_test)

    accuracy = correct / total * 100

    print("\n======================")
    print("MODEL PERFORMANCE")
    print("======================")

    print(f"Correct predictions: {correct}/{total}")
    print(f"Accuracy: {accuracy:.2f}%")

    print("\nPredictions:")
    print(predictions)

    print("\nExpected:")
    print(y_test)

    # -------------------------
    # 8. Visualisation des données
    # -------------------------

    plt.figure()

    plt.scatter(
        X[y == 0, 0],
        X[y == 0, 1],
        label="Class 0"
    )

    plt.scatter(
        X[y == 1, 0],
        X[y == 1, 1],
        label="Class 1"
    )
    x_values = np.linspace(
        X[:, 0].min(),
        X[:, 0].max(),
        100
    )

    if weights[1] != 0:

        y_values = (
            -(weights[0] * x_values + bias)
            / weights[1]
        )

        plt.plot(
            x_values,
            y_values,
            label="Decision boundary"
        )

    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("Perceptron Classification")
    plt.legend()
    plt.show()
    plt.figure()

    plt.plot(
        range(1, len(errors_history) + 1),
        errors_history
    )

    plt.xlabel("Epoch")
    plt.ylabel("Number of errors")
    plt.title("Training Errors")

    plt.show()


if __name__ == "__main__":
    main()