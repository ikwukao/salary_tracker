# =========================================================
# EMPLOYEE CLASS
# =========================================================
# This class represents an employee inside a company.
#
# Features:
# - Stores employee name, level, and salary
# - Validates employee data using property setters
# - Prevents invalid promotions and salary assignments
# - Automatically updates salary during promotion
#
# Concepts Demonstrated:
# - Object-Oriented Programming (OOP)
# - Encapsulation
# - Properties and setters
# - Validation logic
# - Class attributes
# =========================================================
class Employee:

    # -----------------------------------------------------
    # CLASS-LEVEL BASE SALARY CONFIGURATION
    # -----------------------------------------------------
    # Stores the minimum salary assigned to each level.
    #
    # This dictionary acts as:
    # - a salary policy
    # - a promotion reference
    # - a validation source
    # -----------------------------------------------------
    _base_salaries = {
        "trainee": 1000,
        "junior": 2000,
        "mid-level": 3000,
        "senior": 4000,
    }

    # =====================================================
    # CONSTRUCTOR
    # =====================================================
    # Initializes a new employee object.
    #
    # Parameters:
    # name  -> employee name
    # level -> employee job level
    #
    # The constructor uses property setters instead of
    # directly assigning protected attributes so that:
    # - validation rules are enforced
    # - salary is initialized automatically
    # =====================================================
    def __init__(self, name, level):

        # Set employee name
        self.name = name

        # Set employee level
        self.level = level

        # Automatically assign salary based on level
        self.salary = Employee._base_salaries[level]

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================
    # Defines how the object appears when printed.
    #
    # Example:
    # Charlie Brown: trainee
    # =====================================================
    def __str__(self):
        return f"{self.name}: {self.level}"

    # =====================================================
    # DEVELOPER REPRESENTATION
    # =====================================================
    # Defines a more technical representation of the object.
    #
    # Useful for:
    # - debugging
    # - logging
    # - development tools
    #
    # Example:
    # Employee('Charlie Brown', 'trainee')
    # =====================================================
    def __repr__(self):
        return f"Employee('{self.name}', '{self.level}')"

    # =====================================================
    # NAME GETTER
    # =====================================================
    # Returns the employee's name.
    # =====================================================
    @property
    def name(self):
        return self._name

    # =====================================================
    # NAME SETTER
    # =====================================================
    # Validates and updates the employee name.
    #
    # Validation Rules:
    # - name must be a string
    # =====================================================
    @name.setter
    def name(self, new_name):

        # Ensure the new name is a string
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")

        # Update protected name attribute
        self._name = new_name

        # Display update confirmation
        print(f"'name' updated to '{self.name}'.")

    # =====================================================
    # LEVEL GETTER
    # =====================================================
    # Returns the employee's current level.
    # =====================================================
    @property
    def level(self):
        return self._level

    # =====================================================
    # LEVEL SETTER
    # =====================================================
    # Validates and updates employee level.
    #
    # Validation Rules:
    # - level must be a string
    # - level must exist in _base_salaries
    # - employee cannot remain on same level
    # - employee cannot be demoted
    #
    # Side Effects:
    # - automatically updates salary
    # - prints promotion message
    # =====================================================
    @level.setter
    def level(self, new_level):

        # Ensure level is a string
        if not isinstance(new_level, str):
            raise TypeError("'level' must be a string.")

        # Ensure level exists in salary structure
        if new_level not in Employee._base_salaries:
            raise ValueError(
                f"Invalid value '{new_level}' for 'level' attribute."
            )

        # Prevent assigning the same level again
        if hasattr(self, "_level") and new_level == self.level:
            raise ValueError(
                f"'{self.level}' is already the selected level."
            )

        # Prevent demotion to a lower level
        if (
            hasattr(self, "_level")
            and Employee._base_salaries[new_level]
            < Employee._base_salaries[self.level]
        ):
            raise ValueError(
                "Cannot change to lower level."
            )

        # Display promotion confirmation
        print(f"'{self.name}' promoted to '{new_level}'.")

        # Update salary using salary setter
        self.salary = Employee._base_salaries[new_level]

        # Update protected level attribute
        self._level = new_level

    # =====================================================
    # SALARY GETTER
    # =====================================================
    # Returns the employee's current salary.
    # =====================================================
    @property
    def salary(self):
        return self._salary

    # =====================================================
    # SALARY SETTER
    # =====================================================
    # Validates and updates employee salary.
    #
    # Validation Rules:
    # - salary must be numeric
    # - salary cannot be below minimum salary
    #   for the employee's level
    #
    # Side Effects:
    # - prints salary update confirmation
    # =====================================================
    @salary.setter
    def salary(self, new_salary):

        # Ensure salary is numeric
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")

        # Prevent salary below minimum level salary
        if (
            hasattr(self, "_level")
            and new_salary < Employee._base_salaries[self.level]
        ):
            raise ValueError(
                f"Salary must be higher than minimum salary "
                f"${Employee._base_salaries[self.level]}."
            )

        # Update protected salary attribute
        self._salary = new_salary

        # Display salary update confirmation
        print(f"Salary updated to ${self.salary}.")


# =========================================================
# CREATE EMPLOYEE OBJECT
# =========================================================
# Create a new employee named Charlie Brown
# with trainee-level status.
# =========================================================
charlie_brown = Employee("Charlie Brown", "trainee")


# =========================================================
# DISPLAY EMPLOYEE INFORMATION
# =========================================================

# Print employee details
print(charlie_brown)

# Print employee salary
print(f"Base salary: ${charlie_brown.salary}")


# =========================================================
# PROMOTE EMPLOYEE
# =========================================================
# Promote Charlie Brown from trainee to junior.
#
# This automatically:
# - validates promotion
# - updates salary
# - prints confirmation messages
# =========================================================
charlie_brown.level = "junior"
