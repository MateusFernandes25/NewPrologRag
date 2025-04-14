%rules here
is_queen_of(Person, Country) :-  % Rule to check if a person is the queen of a certain country
queen_of(Person, Country). % If the person is the queen of the country in our facts, then the rule holds true.

%Example: is_queen_of(diana, england). This will return true because Diana is the queen of England according to our facts.
