# ===== STEP 1: student inputs =====
LAST_NAME = "Flores"
STUDENT_ID = "TUPM-26-4356"
FAVORITE_ARTIST = "One Direction"

SEED_NUM = int(STUDENT_ID[-1])          # last digit of ID -> 6

# ===== STEP 2: turn the artist's letters into numbers (A=1, B=2, ... Z=26) =====
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
positions = []
for letter in FAVORITE_ARTIST.upper():
    if letter != " ":                    # skip the space
        positions.append(alphabet.index(letter) + 1)

print("Positions:", positions)


# =====================================================
# EXERCISE 1: Engineering Test Data Organizer
# =====================================================
print("\n===== EXERCISE 1 =====")

categories = ["TEMPERATURE", "VOLTAGE", "CURRENT", "PRESSURE", "SPEED"]

# each record is a list: [source, category, value]
records = []
for i in range(5):
    source = LAST_NAME + "_T" + str(i + 1)
    value = SEED_NUM + positions[i]
    records.append([source, categories[i], value])

records.append(records[0].copy())                                     # repeated record
records.append([LAST_NAME + "_T2", "VOLTAGE", SEED_NUM + positions[5]])   # extra VOLTAGE
records.append([LAST_NAME + "_T3", "VOLTAGE", SEED_NUM + positions[6]])   # extra VOLTAGE
records.append([LAST_NAME + "_T4", "PRESSURE", SEED_NUM + positions[7]])  # extra PRESSURE

print("Generated Test Data:")
for r in records:
    print(r)

# find repeated and distinct records
distinct = []
repeated = []
for r in records:
    if r in distinct:
        repeated.append(r)
    else:
        distinct.append(r)

print("Repeated:", repeated)
print("Distinct records:", len(distinct), "of", len(records))

# group values by category using a dictionary
by_category = {}
for r in distinct:
    category = r[1]
    value = r[2]
    if category not in by_category:
        by_category[category] = []
    by_category[category].append(value)

print("\nSummary per category:")
averages = {}
for category in categories:
    values = by_category[category]
    average = sum(values) / len(values)
    averages[category] = round(average, 2)
    print(category, "-> count:", len(values), "min:", min(values),
          "max:", max(values), "avg:", round(average, 2), "sum:", sum(values))

# order categories from highest to lowest average
ordered = sorted(averages, key=averages.get, reverse=True)
print("\nOrdered by average (high to low):", ordered)

all_values = []
for r in distinct:
    all_values.append(r[2])
print("FINAL: total =", sum(all_values),
      "| average =", round(sum(all_values) / len(all_values), 2),
      "| min =", min(all_values), "| max =", max(all_values))


# =====================================================
# EXERCISE 2: Student Performance Data Analyzer
# =====================================================
print("\n===== EXERCISE 2 =====")

subjects = ["PROGRAMMING", "MATHEMATICS", "ELECTRONICS", "PHYSICS", "ENGLISH"]

def make_score(position):
    return 55 + (SEED_NUM * position) % 45      # gives 55 to 99

def get_category(score):
    if score >= 90:
        return "Outstanding"
    elif score >= 85:
        return "Very Satisfactory"
    elif score >= 80:
        return "Satisfactory"
    elif score >= 75:
        return "Fair"
    else:
        return "Needs Improvement"

# each record: [student, subject, score]   (None = missing score)
records = []
for i in range(5):
    records.append([LAST_NAME + "_S" + str(i + 1), subjects[i], make_score(positions[i])])

records.append(records[0].copy())                                              # repeated
records.append([LAST_NAME + "_S1", "MATHEMATICS", make_score(positions[5])])
records.append([LAST_NAME + "_S2", "ELECTRONICS", make_score(positions[6])])
records.append([LAST_NAME + "_S3", "PHYSICS", make_score(positions[7])])
records.append([LAST_NAME + "_S4", "ENGLISH", None])                            # missing score
records.append([LAST_NAME + "_S5", "PROGRAMMING", make_score(positions[8])])

print("Generated Records:")
for r in records:
    print(r)

valid = []
repeated = []
incomplete = []
for r in records:
    if r[2] is None:
        incomplete.append(r)
    elif r in valid:
        repeated.append(r)
    else:
        valid.append(r)

print("\nRepeated:", repeated)
print("Incomplete:", incomplete)
print("Valid unique records:", len(valid))

print("\nPerformance categories:")
for r in valid:
    print(r, "->", get_category(r[2]))

# average per student and per subject
student_scores = {}
subject_scores = {}
for r in valid:
    if r[0] not in student_scores:
        student_scores[r[0]] = []
    student_scores[r[0]].append(r[2])
    if r[1] not in subject_scores:
        subject_scores[r[1]] = []
    subject_scores[r[1]].append(r[2])

student_avg = {}
for name in student_scores:
    student_avg[name] = sum(student_scores[name]) / len(student_scores[name])
subject_avg = {}
for name in subject_scores:
    subject_avg[name] = sum(subject_scores[name]) / len(subject_scores[name])

print("\nStudents (best to lowest average):")
for name in sorted(student_avg, key=student_avg.get, reverse=True):
    print(name, round(student_avg[name], 2))

print("\nSubjects (best to lowest average):")
for name in sorted(subject_avg, key=subject_avg.get, reverse=True):
    print(name, round(subject_avg[name], 2))


# =====================================================
# EXERCISE 3: Transaction History Analyzer
# =====================================================
print("\n===== EXERCISE 3 =====")

products = ["NOTEBOOK", "PEN", "USB", "HEADPHONES", "CALCULATOR"]
prices = {"NOTEBOOK": 45, "PEN": 12, "USB": 350, "HEADPHONES": 899, "CALCULATOR": 520}

def make_qty(position):
    return (SEED_NUM + position) % 9 + 1

# each transaction: [customer, product, quantity]
transactions = []
for i in range(5):
    transactions.append([LAST_NAME + "_C" + str(i + 1), products[i], make_qty(positions[i])])

transactions.append([LAST_NAME + "_C1", "NOTEBOOK", make_qty(positions[5])])   # repeated purchase
transactions.append([LAST_NAME + "_C2", "USB", make_qty(positions[6])])
transactions.append([LAST_NAME + "_C3", "CALCULATOR", make_qty(positions[7])])
transactions.append([LAST_NAME + "_C4", "PEN", make_qty(positions[8])])
transactions.append([LAST_NAME + "_C5", "HEADPHONES", make_qty(positions[9])])

total_all = 0
customer_units = {}
customer_value = {}
product_units = {}
product_value = {}

print("Transactions (customer, product, qty, value):")
for t in transactions:
    customer, product, qty = t[0], t[1], t[2]
    value = qty * prices[product]
    print(customer, product, qty, value)
    total_all = total_all + value

    customer_units[customer] = customer_units.get(customer, 0) + qty
    customer_value[customer] = customer_value.get(customer, 0) + value
    product_units[product] = product_units.get(product, 0) + qty
    product_value[product] = product_value.get(product, 0) + value

print("\nOverall total value:", total_all)
print("Customer summary (units):", customer_units)
print("Customer summary (value):", customer_value)
print("Product summary (units):", product_units)
print("Product summary (value):", product_value)

print("\nCustomers ordered by value:", sorted(customer_value, key=customer_value.get, reverse=True))
print("Products ordered by value:", sorted(product_value, key=product_value.get, reverse=True))