class BinColors:
    HEADER      = '\033[95m'
    OKBLUE      = '\033[94m'
    OKCYAN      = '\033[96m'
    OKGREEN     = '\033[92m'
    WARNING     = '\033[93m'
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'


class Logger:
    
    @staticmethod
    def info(message) -> None:
        print(f'{ BinColors.OKBLUE }[*] { message }{ BinColors.ENDC }')

    @staticmethod
    def success(message) -> None:
        print(f'{ BinColors.OKCYAN }[+] { message }{ BinColors.ENDC }')

    @staticmethod
    def warning(message) -> None:
        print(f'{ BinColors.WARNING }[!] { message }{ BinColors.ENDC }')

    @staticmethod
    def fail(message) -> None:
        print(f'{ BinColors.FAIL }[-] { message }{ BinColors.ENDC }')


if __name__ == '__main__':
    Logger.info('this is info')
    Logger.success('this is success')
    Logger.warning('this is warning')
    Logger.fail('this is fail')