import concurrent.futures

def parallel_factorial(number):
    if not isinstance(number, int):
        raise TypeError("The given input is not a number")
    if number < 0:
        raise ValueError("The input number must be greater than zero or positive")

    def chunk_factorial(start, end):
        result = 1
        for i in range(start, end + 1):
            result *= i
        return result

    def factorial(number):
        if number <= 1:
            return 1

        # Divide the range into chunks
        chunk_size = number // 4
        ranges = [(i * chunk_size + 1, (i + 1) * chunk_size) for i in range(4)]
        # Adjust the last range to include the remainder
        ranges[-1] = (ranges[-1][0], number)

        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = list(executor.map(lambda r: chunk_factorial(r[0], r[1]), ranges))

        final_result = 1
        for res in results:
            final_result *= res

        return final_result

    return factorial(number)

print(parallel_factorial(36))
