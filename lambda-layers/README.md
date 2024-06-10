# AWS Lambda Layers

This directory contains the definition and implementation of the AWS Lambda layers used in the project.

## Layers

The following layers are defined in this project:

1. **Python Common Dependencies Layer**
2. **Hello Module Layer**
3. **Pyodbc Layer**

Each layer is defined using the AWS Serverless Application Model (SAM) and can be deployed to your AWS account using the AWS CLI or AWS SAM CLI.

## Python Common Dependencies Layer

The `PythonCommonDependencies` layer contains the following common Python dependencies:

- `requests`: A popular library for making HTTP requests in Python.
- `numpy`: A fundamental library for scientific computing in Python, providing support for large, multi-dimensional arrays and matrices.
- `pandas`: A powerful data analysis and manipulation library for Python, providing high-performance, easy-to-use data structures and data analysis tools.

This layer is compatible with the following Python runtimes:

- `python3.7`
- `python3.8`
- `python3.9`
- `python3.10`
- `python3.11`
- `python3.12`

The layer is defined in the `PythonCommonDependencies` directory, and the `template.yaml` file in this directory contains the SAM definition for the layer.

## Hello Module Layer

The `HelloModule` layer contains a custom Python module with a simple "hello" function. This layer is used to demonstrate the usage of a custom layer in a Lambda function.

The module is defined in the `hello.py` file, and the layer is defined in the `HelloModule` directory using the `template.yaml` file.

This layer is compatible with the same Python runtimes as the `PythonCommonDependencies` layer.

## Pyodbc Layer

The `Pyodbc` layer contains the `pyodbc` library, which is used for connecting to SQL databases. This library is often used in data-intensive applications that require access to relational databases.

This layer is compatible with the following Python runtimes:

- `python3.8`
- `python3.9`
- `python3.10`
- `python3.11`
- `python3.12`

The layer is defined in the `Pyodbc` directory, and the `template.yaml` file in this directory contains the SAM definition for the layer.

## Deployment

To deploy the layers, you can use the AWS SAM CLI or the AWS CLI. The deployment process is defined in the `template.yaml` file in the root directory of the repository.

For more information on how to deploy the layers, please refer to the main README.md file.

## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
