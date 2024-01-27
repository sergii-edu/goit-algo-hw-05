from timeit import timeit
from tabulate import tabulate

from helpers.knuth_morris_pratt_search import kmp_search
from helpers.boyer_moore_search import boyer_moore_search
from helpers.rabin_karp_search import rabin_karp_search


def load_file(filename):
    with open(filename, "r") as file:
        return file.read()


def test_search(article, test_substring):
    return {
        "Knuth-Morris-Pratt": timeit(
            lambda: kmp_search(article, test_substring), number=100
        ),
        "Boyer-Moore": timeit(
            lambda: boyer_moore_search(article, test_substring), number=100
        ),
        "Rabin-Karp": timeit(
            lambda: rabin_karp_search(article, test_substring), number=100
        ),
    }


def main():
    article_1 = load_file("./data/article_1.txt")
    article_2 = load_file("./data/article_2.txt")

    article_1_success_search = test_search(
        article_1, "Також, у теорії алгоритмів жадібні"
    )
    article_1_fail_search = test_search(
        article_1, "дослідження, що складається з наступних"
    )
    article_2_success_search = test_search(
        article_2, "досягнення поставленої мети визначена"
    )
    article_2_fail_search = test_search(
        article_2, "можна дробити так само на підзадачі; "
    )

    def get_average(name):
        numbers = [
            article_1_success_search.get(name),
            article_1_fail_search.get(name),
            article_2_success_search.get(name),
            article_2_fail_search.get(name),
        ]
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        return average

    print(
        tabulate(
            [
                ["Article 1, success search"] + list(article_1_success_search.values()),
                ["Article 1, fail search"] + list(article_1_fail_search.values()),
                ["Article 2, success search"] + list(article_2_success_search.values()),
                ["Article 2, fail search"] + list(article_2_fail_search.values()),
                [
                    "Average time",
                    get_average("Knuth-Morris-Pratt"),
                    get_average("Boyer-Moore"),
                    get_average("Rabin-Karp"),
                ],
            ],
            headers=["", "Knuth-Morris-Pratt", "Boyer-Moore", "Rabin-Karp"],
            tablefmt="grid",
        )
    )


if __name__ == "__main__":
    main()
