total_second=int(input("Enter seconds: "))
hours=total_second//3600
remaining_seconds=total_second%3600
minutes=remaining_seconds//60

final_second=remaining_seconds % 60

print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Final_second: {final_second}")