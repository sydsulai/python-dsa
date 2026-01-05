class ExtractionOfDigits:
    def extract_digits(self, number: int):
        n = number
        while n > 0:
            last_digit = n % 10
            print(last_digit)
            n = n//10
        
        return "Extraction Complete"
    
if __name__ == "__main__":
    extractor = ExtractionOfDigits()
    result = extractor.extract_digits(12345)
    print(result)