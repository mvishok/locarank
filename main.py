import colorama
from colorama import Fore, Style
import factors.const as const
from factors import education, finance, health, entertainment
colorama.init(autoreset=True)


def calculate_total_score(scores):

    total_score = 0

    for category, score in scores.items():
        weight = const.CATEGORY.get(category, 0)
        total_score += score * weight

    return total_score

def main():
    print(Fore.BLUE + Style.BRIGHT + "LOCARANK Beta" + Style.RESET_ALL)

    latitude = float(input(Fore.GREEN + "Enter latitude: " + Style.RESET_ALL))
    longitude = float(input(Fore.GREEN + "Enter longitude: " + Style.RESET_ALL))

    print(Fore.BLUE + "\nCalculating scores..." + Style.RESET_ALL)

    category_scores = {
        'Education': education.get_education(latitude, longitude, Fore, Style),
        'Healthcare': health.get_health(latitude, longitude, Fore, Style),
        'Finance': finance.get_finance(latitude, longitude, Fore, Style),
        'Entertainment': entertainment.get_entertainment(latitude, longitude, Fore, Style)
    }

    total_score = calculate_total_score(category_scores)

    print(Fore.BLUE + "\nResults:" + Style.RESET_ALL)
    print(Fore.CYAN + f"Total Score: {total_score:.2f}" + Style.RESET_ALL)

    if total_score >= 80:
        print(Fore.GREEN + "The location is highly suitable!" + Style.RESET_ALL)
    elif total_score >= 60:
        print(Fore.YELLOW + "The location is moderately suitable." + Style.RESET_ALL)
    else:
        print(Fore.RED + "The location is not very suitable." + Style.RESET_ALL)

if __name__ == "__main__":
    main()