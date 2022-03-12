from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        # My work --------------------
        if self.is_complete(assignment):
            return assignment

        var = self.select_unassigned_variable(assignment)

        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                # add value
                assignment[var] = value

                result = self.recursive_backtracking(assignment)
                if result != None:
                    return result

                # remove value
                del assignment[var]

        # return failure
        return None
        # My work --------------------

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_south_america_csp():

    CostaRica, Panama, Colombia, \
    Venezuela, Ecuador, Peru, \
    Guyana, Suriname, Guyane_Fr, \
    Brazil, Bolivia, Paraguay, \
    Chile, Uruguay, Argentina, \
    Falkland_Islands = \
        'CostaRica', 'Panama', 'Colombia', \
        'Venezuela', 'Ecuador', 'Peru', \
        'Guyana', 'Suriname', 'Guyane_Fr', \
        'Brazil', 'Bolivia', 'Paraguay', \
        'Chile', 'Uruguay', 'Argentina', \
        'Falkland_Islands'
    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [CostaRica, Panama, Colombia, 
                Venezuela, Ecuador, Peru, 
                Guyana, Suriname, Guyane_Fr, 
                Brazil, Bolivia, Paraguay, 
                Chile, Uruguay, Argentina, 
                Falkland_Islands]
    domains = {
        CostaRica: values[:],
        Panama: values[:],
        Colombia: values[:],
        Venezuela: values[:],
        Ecuador: values[:],
        Peru: values[:],
        Guyana: values[:],
        Suriname: values[:],
        Guyane_Fr: values[:],
        Brazil: values[:],
        Bolivia: values[:],
        Paraguay: values[:],
        Chile: values[:],
        Uruguay: values[:],
        Argentina: values[:],
        Falkland_Islands: values[:]
    }
    neighbours = {
        CostaRica: [Panama],
        Panama: [CostaRica, Colombia],
        Colombia: [Panama, Ecuador, Peru, Brazil, Venezuela],
        Venezuela: [Colombia, Brazil, Guyana],
        Ecuador: [Colombia, Peru],
        Peru: [Ecuador, Colombia, Brazil, Bolivia, Chile],
        Guyana: [Venezuela, Brazil, Suriname],
        Suriname: [Guyana, Brazil, Guyane_Fr],
        Guyane_Fr: [Suriname, Brazil],
        Brazil: [Guyane_Fr, Suriname, Guyana, Venezuela, Colombia, Peru, Bolivia, Paraguay, Argentina, Uruguay],
        Bolivia: [Peru, Brazil, Paraguay, Argentina, Chile],
        Paraguay: [Bolivia, Brazil, Argentina],
        Chile: [Peru, Bolivia, Argentina],
        Uruguay: [Brazil, Argentina],
        Argentina: [Chile, Bolivia, Paraguay, Brazil, Uruguay],
        Falkland_Islands: []
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        CostaRica: constraint_function,
        Panama: constraint_function,
        Colombia: constraint_function,
        Venezuela: constraint_function,
        Ecuador: constraint_function,
        Peru: constraint_function,
        Guyana: constraint_function,
        Suriname: constraint_function,
        Guyane_Fr: constraint_function,
        Brazil: constraint_function,
        Bolivia: constraint_function,
        Paraguay: constraint_function,
        Chile: constraint_function,
        Uruguay: constraint_function,
        Argentina: constraint_function,
        Falkland_Islands: constraint_function
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    south_america = create_south_america_csp()
    result = south_america.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/americas.html
