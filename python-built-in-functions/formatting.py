class Formatter:
    @staticmethod
    def as_currency(value):
        return f"${value:,.2f}"

    @staticmethod
    def as_percent(value):
        return f"{value:.2%}"
