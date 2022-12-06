# Configs data base
from Database import load
# Exibe lista de transações redo
from ShowTransactionsRedo import showTransactionsRedo


def main():
   load()


if __name__ == '__main__':
   load()
   showTransactionsRedo()