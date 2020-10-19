
class _job_center_database:

       def __init__(self):
        self.boroughs = dict()
        self.job_center_names = dict()
        self.addresses = dict()
        self.phone_numbers = dict()
        self.comments = dict()
        # could add long lat

       def load_job_centers(self, job_center_file):
        f = open(movie_file)
        for job_center_id, line in enumerate(f):
                line = line.rstrip()
                components = line.split(",")
                borough = components[0]
                jcname = components[1]
                address = ' '.join(components[2:6])
                phone_number = components[6]
                comment = components[7]
                print("The ID is", job_center_id, "and the name is", jcname, "and address is", address, "!")
                self.boroughs[job_center_id] = borough
                self.job_center_names[job_center_id] = jcname
                self.addresses[job_center_id] = address
                self.phone_numbers[job_center_id] = phone_number
                self.comments[job_center_id] = [comment]
        f.close()

       def get_job_centers(self):
        return self.job_center_names.keys()

       def get_job_center(self, jcid):
        try:
                jcname = self.job_center_names[jcid]
                borough = self.boroughs[jcid]
                addresss = self.addresses[jcid]
                phone_number = self.phone_numbers[jcid]
                comments = self.comments[jcid]

                job_center = list((jcname, borough, address, phone_number, comments))
        except Exception as ex:
                job_center = None
        return job_center

       def set_job_center(self, jcid, job_center):
        self.job_center_names[jcid] = job_center[0]
        self.boroughs[jcid] = job_center[1]
        self.addresses[jcid] = job_center[2]
        self.phone_numbers[jcid] = job_center[3]
        self.comments[jcid] = job_center[4]


       def delete_job_center(self, jcid):
        del(self.job_center_names[jcid])
        del(self.movie_boroughs[jcid])
        del(self.addresses[jcid])
        del(self.phone_numbers[jcid])
        del(self.comments[jcid])


       def get_comments(self, jcid): #Need to update this to handle strings not numbers
        return (self.comments[jcid])

   
       def delete_all_comments(self):
        for jcid in self.get_comments():
                self.comments[jcid] = []

if __name__ == "__main__":
       jcdb = _job_center_database()

       #### JOB Centers ########
       jcdb.load_job_centers('Directory_Of_Job_Centers.csv')

       job_center = jcdb.get_job_center(2)
       print(job_center[0])

       job_center[0] = 'ABC'
       mdb.set_job_center(2, job_center)

       print("A")
       print(jcdb.get_comments(3))
       print("B")

       job_center = jcdb.get_job_center(2)
       print(job_center[0])
       ####################

       #### COMMENTS #######
      

       comments = jcdb.get_comments(1)
       print(comments)

       ####################

