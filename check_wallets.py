def load_wallets(file_path):
    """
    Загружает список кошельков из указанного файла.
    
    :param file_path: Путь к файлу с кошельками
    :return: Список кошельков
    """
    with open(file_path, 'r') as file:
        wallets = [line.strip().lower() for line in file if line.strip()]
    return wallets

def check_wallet(wallet_to_check, wallet_list):
    """
    Проверяет, есть ли указанный кошелек в списке кошельков.
    
    :param wallet_to_check: Кошелек, который нужно проверить
    :param wallet_list: Список кошельков
    :return: Сообщение о результате проверки
    """
    wallet_to_check = wallet_to_check.strip().lower()
    if wallet_to_check in wallet_list:
        return f'Кошелек {wallet_to_check} найден в списке.'
    else:
        return f'Кошелек {wallet_to_check} не найден в списке.'

def check_wallets_in_list(wallets_to_check, wallet_list):
    """
    Проверяет список кошельков на наличие в другом списке.
    
    :param wallets_to_check: Список кошельков для проверки
    :param wallet_list: Список всех кошельков
    :return: Список сообщений о результате проверки для каждого кошелька
    """
    results = []
    for wallet in wallets_to_check:
        result = check_wallet(wallet, wallet_list)
        results.append(result)
    return results

# Пример использования функции
if __name__ == "__main__":
    wallets_file_path = 'wallets.txt'
    wallets_to_check_file_path = 'wallets_to_check.txt'
    
    wallets = load_wallets(wallets_file_path)
    wallets_to_check = load_wallets(wallets_to_check_file_path)
    
    results = check_wallets_in_list(wallets_to_check, wallets)
    for result in results:
        print(result)
