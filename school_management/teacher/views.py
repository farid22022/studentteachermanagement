from django.shortcuts import render

# Create your views here.
def profile(request):
    teacher = {
        "CSE Department": [
            {"name": "Dr. Jane Smith", "email": "jane.smith@university.edu", "phone": "123-456-7890", "salary": 75000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. John Doe", "email": "john.doe@university.edu", "phone": "987-654-3210", "salary": 70000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Alice Brown", "email": "alice.brown@university.edu", "phone": "123-456-7891", "salary": 78000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Robert Green", "email": "robert.green@university.edu", "phone": "987-654-3211", "salary": 72000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Laura White", "email": "laura.white@university.edu", "phone": "123-456-7892", "salary": 76000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Michael Black", "email": "michael.black@university.edu", "phone": "987-654-3212", "salary": 74000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Olivia Blue", "email": "olivia.blue@university.edu", "phone": "123-456-7893", "salary": 77000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"}
        ],
        "ECE Department": [
            {"name": "Dr. Emily Johnson", "email": "emily.j@university.edu", "phone": "555-123-4567", "salary": 80000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. David Wilson", "email": "david.wilson@university.edu", "phone": "555-123-4568", "salary": 79000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Sophia Martinez", "email": "sophia.m@university.edu", "phone": "555-123-4569", "salary": 81000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. James Anderson", "email": "james.a@university.edu", "phone": "555-123-4570", "salary": 82000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Emma Taylor", "email": "emma.t@university.edu", "phone": "555-123-4571", "salary": 83000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Noah Thomas", "email": "noah.t@university.edu", "phone": "555-123-4572", "salary": 84000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Ava Jackson", "email": "ava.j@university.edu", "phone": "555-123-4573", "salary": 85000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"}
        ],
        "Math Department": [
        {"name": "Prof. Alan Walker", "email": "alan.walker@university.edu", "phone": "444-321-6789", "salary": 72000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
        {"name": "Dr. Mia Harris", "email": "mia.harris@university.edu", "phone": "444-321-6790", "salary": 73000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
        {"name": "Prof. Lucas Clark", "email": "lucas.clark@university.edu", "phone": "444-321-6791", "salary": 74000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
        {"name": "Dr. Ella Lewis", "email": "ella.lewis@university.edu", "phone": "444-321-6792", "salary": 75000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
        {"name": "Prof. Mason Young", "email": "mason.young@university.edu", "phone": "444-321-6793", "salary": 76000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
        {"name": "Dr. Lily Hall", "email": "lily.hall@university.edu", "phone": "444-321-6794", "salary": 77000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
        {"name": "Prof. Ethan Allen", "email": "ethan.allen@university.edu", "phone": "444-321-6795", "salary": 78000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"}
        ],
        "Physics Department": [
            {"name": "Dr. Sarah Lee", "email": "sarah.lee@university.edu", "phone": "333-678-2345", "salary": 76000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. William Brown", "email": "william.brown@university.edu", "phone": "222-345-6789", "salary": 78000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Chloe King", "email": "chloe.king@university.edu", "phone": "333-678-2346", "salary": 77000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Daniel Scott", "email": "daniel.scott@university.edu", "phone": "222-345-6790", "salary": 79000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Grace Adams", "email": "grace.adams@university.edu", "phone": "333-678-2347", "salary": 80000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Henry Baker", "email": "henry.baker@university.edu", "phone": "222-345-6791", "salary": 81000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Zoe Carter", "email": "zoe.carter@university.edu", "phone": "333-678-2348", "salary": 82000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"}
        ],
        "Chemistry Department": [
            {"name": "Dr. Rachel Adams", "email": "rachel.adams@university.edu", "phone": "555-678-1234", "salary": 82000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Nathan Turner", "email": "nathan.turner@university.edu", "phone": "555-678-1235", "salary": 83000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Hannah Parker", "email": "hannah.parker@university.edu", "phone": "555-678-1236", "salary": 84000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Samuel Evans", "email": "samuel.evans@university.edu", "phone": "555-678-1237", "salary": 85000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Victoria Collins", "email": "victoria.collins@university.edu", "phone": "555-678-1238", "salary": 86000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Andrew Stewart", "email": "andrew.stewart@university.edu", "phone": "555-678-1239", "salary": 87000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Samantha Morris", "email": "samantha.morris@university.edu", "phone": "555-678-1240", "salary": 88000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"}
        ],
        "Biology Department": [
            {"name": "Prof. Benjamin King", "email": "benjamin.king@university.edu", "phone": "111-234-8901", "salary": 74000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Abigail Wright", "email": "abigail.wright@university.edu", "phone": "111-234-8902", "salary": 75000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Jack Hughes", "email": "jack.hughes@university.edu", "phone": "111-234-8903", "salary": 76000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Evelyn Price", "email": "evelyn.price@university.edu", "phone": "111-234-8904", "salary": 77000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Owen Bennett", "email": "owen.bennett@university.edu", "phone": "111-234-8905", "salary": 78000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Scarlett Wood", "email": "scarlett.wood@university.edu", "phone": "111-234-8906", "salary": 79000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Leo Brooks", "email": "leo.brooks@university.edu", "phone": "111-234-8907", "salary": 80000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"}
        ],
        "English Department": [
            {"name": "Dr. Sophia Carter", "email": "sophia.carter@university.edu", "phone": "666-789-1234", "salary": 73000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Logan Phillips", "email": "logan.phillips@university.edu", "phone": "666-789-1235", "salary": 74000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Harper Foster", "email": "harper.foster@university.edu", "phone": "666-789-1236", "salary": 75000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Aiden Sanders", "email": "aiden.sanders@university.edu", "phone": "666-789-1237", "salary": 76000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Addison Reed", "email": "addison.reed@university.edu", "phone": "666-789-1238", "salary": 77000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Ellie Murphy", "email": "ellie.murphy@university.edu", "phone": "666-789-1239", "salary": 78000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Stella Rivera", "email": "stella.rivera@university.edu", "phone": "666-789-1240", "salary": 79000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"}
        ],
        "History Department": [
            {"name": "Dr. Nora Bell", "email": "nora.bell@university.edu", "phone": "777-890-1234", "salary": 72000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Julian Gray", "email": "julian.gray@university.edu", "phone": "777-890-1235", "salary": 73000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Hazel Ross", "email": "hazel.ross@university.edu", "phone": "777-890-1236", "salary": 74000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Gabriel Cox", "email": "gabriel.cox@university.edu", "phone": "777-890-1237", "salary": 75000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Violet Howard", "email": "violet.howard@university.edu", "phone": "777-890-1238", "salary": 76000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Luke Ward", "email": "luke.ward@university.edu", "phone": "777-890-1239", "salary": 77000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Aurora Torres", "email": "aurora.torres@university.edu", "phone": "777-890-1240", "salary": 78000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"}
        ],
        "Economics Department": [
            {"name": "Dr. Penelope Peterson", "email": "penelope.peterson@university.edu", "phone": "888-901-2345", "salary": 80000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Christopher Murray", "email": "christopher.murray@university.edu", "phone": "888-901-2346", "salary": 81000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Naomi Flores", "email": "naomi.flores@university.edu", "phone": "888-901-2347", "salary": 82000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Isaac Butler", "email": "isaac.butler@university.edu", "phone": "888-901-2348", "salary": 83000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Eleanor Simmons", "email": "eleanor.simmons@university.edu", "phone": "888-901-2349", "salary": 84000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Aaron Foster", "email": "aaron.foster@university.edu", "phone": "888-901-2350", "salary": 85000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Clara Bryant", "email": "clara.bryant@university.edu", "phone": "888-901-2351", "salary": 86000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"}
        ],
        "Psychology Department": [
            {"name": "Dr. Lily Alexander", "email": "lily.alexander@university.edu", "phone": "999-012-3456", "salary": 75000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Joshua Russell", "email": "joshua.russell@university.edu", "phone": "999-012-3457", "salary": 76000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Zoe Griffin", "email": "zoe.griffin@university.edu", "phone": "999-012-3458", "salary": 77000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Elijah Diaz", "email": "elijah.diaz@university.edu", "phone": "999-012-3459", "salary": 78000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Stella Hayes", "email": "stella.hayes@university.edu", "phone": "999-012-3460", "salary": 79000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Prof. Levi Myers", "email": "levi.myers@university.edu", "phone": "999-012-3461", "salary": 80000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"},
            {"name": "Dr. Maya Ford", "email": "maya.ford@university.edu", "phone": "999-012-3462", "salary": 81000, "photo": "https://i.ibb.co.com/h1HYvpNn/images-removebg-preview.png"}
        ],
        }
    
    return render(request, 'teacher/index.html', {'teacher': teacher})
