def _safe_int(prompt):
	"""Prompt until the user enters a valid integer."""
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			print("Please enter a valid integer.")


def main():
	rent = _safe_int("Enter the total rent amount: ")
	food = _safe_int("Enter the total food expenses: ")
	electricity = _safe_int("Enter the total electricity bill: ")
	charge = _safe_int("Enter the charge per unit of electricity: ")
	water = _safe_int("Enter the total water bill: ")
	members = _safe_int("Enter the number of members living in the house: ")

	# Compute electricity units (guard against zero charge)
	if charge == 0:
		total_electricity_units = None
		print("Warning: charge per unit is 0 — cannot compute electricity units.")
	else:
		total_electricity_units = electricity / charge

	total_expenses = rent + food + electricity + water

	# Compute share per member (guard against zero/negative members)
	if members <= 0:
		share_per_member = None
		print("Warning: number of members must be > 0 to compute per-person share.")
	else:
		share_per_member = total_expenses / members

	print("\nSummary:")
	if total_electricity_units is None:
		print("Total electricity units: n/a")
	else:
		print(f"Total electricity units (approx): {total_electricity_units:.2f}")
	print(f"Total expenses: {total_expenses}")
	if share_per_member is None:
		print("Share per member: n/a")
	else:
		print(f"Share per member: {share_per_member:.2f}")


if __name__ == '__main__':
	main()