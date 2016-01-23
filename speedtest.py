from eventity import ecs, System
import time
component = {
    "name": "comp",
    "data": {
        "string": "BOOOOYAH"
    }
}
test_list = []
class TestSystem(System):
    def set_up(self, evt):
        evt.subscribe(self.adjust_strings, "make_hello")

    def adjust_strings(self, data):
        for ent in self.ecs.list(["comp"]):
            ent.comp["string"] = data["new_string"]


add_time1 = time.time()
for x in xrange(100000):
    ecs.new().add(component)
add_time2 = time.time()
print "Making 100000 components: " + str(add_time2 - add_time1) + " seconds"

search_time1 = time.time()
for e in ecs.list(["comp", "Thing", "another"]):
    test_list.append(e)

for e in ecs.list(["comp", "Thing", "another"]):
    test_list.append(e)

for e in ecs.list(["comp", "Thing", "another"]):
    test_list.append(e)

for e in ecs.list(["comp", "Thing", "another"]):
    test_list.append(e)
search_time2 = time.time()
print "Searching all those 100000 components 4 times: " + str(search_time2 - search_time1) + " seconds"

system_time1 = time.time()
ecs.register(TestSystem)
ecs.send("make_hello", {"new_string": "Mang"})
ecs.send("make_hello", {"new_string": "Trudy"})
ecs.send("make_hello", {"new_string": "Oliver"})
ecs.send("make_hello", {"new_string": "Phil"})
system_time2 = time.time()
print "Registering a system and making lots of expensive calls: " + str(system_time2 - system_time1) + " seconds"
