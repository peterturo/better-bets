from app.email_service import send_email

if __name__ == "__main__":

    print("ARBITRAGE EMAIL...")


    # keeping the email content simple for example purposes, but
    # ... for an example of attaching the data as a CSV file
    # ... and attaching the chart as an image file
    # ... see: https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/codebase-cleanup/starter/app/unemployment_email.py#L56-L132
    # ... (you might need to create a more complex email sending function)

    html_content = f"""
        <h3>Arbitrage Bets</h3>
        <p> </p>
    """


    send_email(subject="[Daily Briefing] Arbitrage Bets", html=html_content)