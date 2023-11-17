class Falcon9:
    def __init__(self, launch_number, current_status):
        self.launch_number = launch_number
        self.launch_dates = []
        self.current_status = current_status
        self.fuel = 0

    def launch(self, date):
        if self.fuel > 0:
            print(f"SpaceX Falcon 9 - Launch #{self.launch_number} on {date} has been launched!")
            self.current_status = "In flight"
            self.fuel -= 1
            self.launch_dates.append(date)
        else:
            print(f"SpaceX Falcon 9 - Launch #{self.launch_number} on {date} has no fuel and cannot be launched.")

    def refuel(self, amount):
        self.fuel += amount
        print(f"SpaceX Falcon 9 - Launch #{self.launch_number} on {self.get_last_launch_date()} has been refueled with {amount} units of fuel.")

    def status(self):
        print(f"SpaceX Falcon 9 - Launch #{self.launch_number} on {self.get_last_launch_date()} - Current Status: {self.current_status}")

    def get_last_launch_date(self):
        if (len(self.launch_dates) > 0):
            return self.launch_dates[len(self.launch_dates) - 1]
        return None;

    def show_all_launch_dates (self):
        print('Launch dates of Falcon 9:')
        if (len(self.launch_dates) == 0):
            print('None')
        else:
            for date in self.launch_dates:
                print(f'\t - {date}')

# testing
falcon9_obj_one = Falcon9('launch-01' , 'Created')
falcon9_obj_one.show_all_launch_dates()
falcon9_obj_one.refuel(3)
falcon9_obj_one.launch('2020-03-01')
falcon9_obj_one.launch('2020-03-02')
falcon9_obj_one.launch('2020-03-03')
falcon9_obj_one.show_all_launch_dates()