# Virtual Room Planner (CLI) Project
# Mini Project - Vaishalini V

def get_user_input():
    print("\n=== Virtual Room Planner ===")
    room_type = input("Enter Room Type (Bedroom/Living Room/Kitchen): ").strip().title()
    budget = int(input("Enter your Budget (in ₹): "))
    color = input("Enter Preferred Color: ").strip().title()
    return room_type, budget, color

def recommend_room(room_type, budget, color):
    # Room styles with base cost
    room_styles = {
        "Bedroom": {"style": "Modern Cozy Bedroom", "base_cost": 20000},
        "Living Room": {"style": "Contemporary Living Room", "base_cost": 35000},
        "Kitchen": {"style": "Minimalist Kitchen", "base_cost": 30000}
    }

    # Color placement ideas
    color_placements = {
        "Violet": {"Walls": "Lavender", "Bed/Seats": "Violet", "Curtains": "Soft Purple", "Decor": "White & Silver"},
        "Blue": {"Walls": "Sky Blue", "Bed/Seats": "Navy Blue", "Curtains": "Light Gray", "Decor": "White & Metallic"},
        "Red": {"Walls": "Light Coral", "Bed/Seats": "Crimson", "Curtains": "Beige", "Decor": "Gold & White"},
        "Green": {"Walls": "Mint Green", "Bed/Seats": "Emerald", "Curtains": "Cream", "Decor": "White & Wood"}
    }

    style_info = room_styles.get(room_type, {"style": "Custom Room", "base_cost": budget})
    colors = color_placements.get(color, {"Walls": color, "Bed/Seats": color, "Curtains": color, "Decor": "Neutral"})

    recommendation = {
        "style": style_info["style"],
        "budget_fit": "✅ Within ₹{}".format(budget) if style_info["base_cost"] <= budget else "⚠ Exceeds budget",
        "color_scheme": colors,
        "estimated_cost": style_info["base_cost"]
    }

    return recommendation

def display_output(recommendation):
    print("\n=== Room Recommendation Report ===")
    print("🏠 Room Style:", recommendation["style"])
    print("💰 Budget Fit:", recommendation["budget_fit"])
    print("\n🎨 Color Placement:")
    for place, col in recommendation["color_scheme"].items():
        print(f"   - {place}: {col}")
    print("\n🛋 Estimated Cost: ₹", recommendation["estimated_cost"])
    print("=================================\n")

def main():
    while True:
        room_type, budget, color = get_user_input()
        recommendation = recommend_room(room_type, budget, color)
        display_output(recommendation)

        # Ask user if they want to try again
        again = input("Do you want to plan another room? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nThank you for using Virtual Room Planner! 👋")
            break

if __name__ == "__main__":
    main()
