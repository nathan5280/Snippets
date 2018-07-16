"""Calculator Server that exposes the RESTful API."""
from server import CalculatorServer

if __name__ == '__main__':
    server = CalculatorServer()
    server.run()
