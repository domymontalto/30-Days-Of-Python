import statistics
import math

class  Statistics:

    def __init__(self, ages):
        self.ages = ages

    def count(self):
        return len(self.ages)
    
    def sum(self):
        return sum(self.ages)
    
    def min(self):
        return min(self.ages)
    
    def max(self):
        return max(self.ages)
    
    def range(self):
        return max(self.ages) - min(self.ages)
    
    def mean(self):
        return math.ceil((sum(self.ages) / len(self.ages)))
    
    def median(self):
        self.ages.sort()
        return self.ages[int(len(self.ages) / 2)]
    
    def mode(self):
        numbers = {}
        for n in self.ages:
            if n not in numbers:
                numbers[n] = 1
            else:
                numbers[n] += 1
        most_common = sorted(numbers.items(), key= lambda x : x[1], reverse=True)
        return most_common[0]
    
    def std(self):
        mean = self.mean()
        std  = 0

        for n in self.ages:
            distance = n - mean
            sq_distance = distance ** 2
            std += sq_distance
        
        average = std / len(self.ages)
        std = math.sqrt(average)
        return round(std, 2)
    
    def var(self):
        mean = self.mean()
        var = []

        for n in self.ages:
            distance = n - mean
            sq_distance = distance ** 2
            var.append(sq_distance)
        
        return sum(var) / len(var)
    
    def freq_dist(self):
        numbers = {}
        
        for n in self.ages:
            if n not in numbers:
                numbers[n] = 1
            else:
                numbers[n] += 1

        for key, value in numbers.items():
            numbers[key] = (value / len(self.ages)) * 100
        
        sorted_numbers = sorted(numbers.items(), key= lambda k : k[1], reverse=True)
        return sorted_numbers




ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

print()

class PersonAccount:

    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes= incomes
        self.expenses = expenses


    def total_income(self):
        if self.incomes != {}:
            return f'Total income: {sum(self.incomes.values())}'
        else:
            return 'No incomes'
    
    def total_expenses(self):
        if self.expenses != {}:
            return f'Total expenses: {sum(self.expenses.values())}'
        else:
            return 'No expences'
        
    def account_info(self):
        return f'Account owner: {self.firstname} {self.lastname}'
    
    def add_income(self, income, description):
        self.incomes[description] = income

    def add_expense(self, expense, description):
        self.expenses[description] = expense

    def account_balance(self):
        if self.expenses == {}:
            return f'Total balance is: {sum(self.incomes.values())}'
        elif self.incomes == {}:
            return f'Total balance is: {sum(self.expenses.values()) * -1}'
        else:
            return f'Total balance is: {sum(self.incomes.values()) - sum(self.expenses.values())}'
    

p = PersonAccount('Dom', 'Mont', {}, {})

p.add_expense(5,'testing')

p.add_income(10, 'test')

print(p.account_info())
print()
print(p.total_income())
print()
print(p.total_expenses())
print()
print(p.account_balance())