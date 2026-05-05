from leads import get_leads
from leads.ai import qualify_lead
from leads.ai.outreach import send_email

def run():
    leads = get_leads()

    for lead in leads:
        score = qualify_lead(lead)

        print(f"{lead['name']} → {score}")

        if score == "HIGH":
            send_email(
                lead["email"],
                "Quick question about your business",
                f"Hey {lead['name']}, I found your profile and had a quick question..."
            )

if __name__ == "__main__":
    run()