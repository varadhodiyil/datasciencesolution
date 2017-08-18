var app = angular.module("recommenderApp", []);
app.config(['$locationProvider', function($locationProvider){
    $locationProvider.html5Mode({
  		enabled: true,
  		requireBase: false
	});
}]);
app.controller("searchCtrl", function ($scope, $http,$location) 
{
    var searched = $location.search();
    $scope.products = [
        {
            "product": "Milk Whole",
            "price": "$4.99",
            "image": "/static/assets/images/recommender/milk.jpg",
            "description": "Milk containing the 3½ percent milk fat that is present when it comes from the cow. None of the milk fat is removed. "
        },
        {
            "product": "Milk 2 Percent",
            "price": "$5.49",
            "image": "/static/assets/images/recommender/milk_2.jpg",
            "description": "Two percent milk contains 140 calories per one cup serving, 5 g of fat, 14 g of carbohydrates" +
            "and 10 g of protein. Sugar content runs high in 2 percent milk, contributing 13 g to the " +
            "carbohydrate content. On the other hand, saturated fat makes up only 3 g of the total fat content. "
        },
        {
            "product": "Milk 1 Percent",
            "price": "$6.49",
            "image": "/static/assets/images/recommender/milk_2.jpg",
            "description": "Ingredients: all natural Grade A lowfat milk, all natural nonfat milk, vitamin A palmitate, vitamin D3. "
        },
        {
            "product": "Milk Fat Free",
            "price": "$8",
            "image": "/static/assets/images/recommender/milk_fat_free.jpeg",
            "description": "Skimmed milk (around 0.1% fat) – Plastic litre bottles are marketed in red packaging. Traditionally this " +
            "used to be delivered in glass bottles with a silver foil lid with a blue checked pattern would be " +
            "colloquially called 'blue-top'. "
        },
        {
            "product": "Apple",
            "price": "$3.99",
            "image": "/static/assets/images/recommender/apple.jpg",
            "description": "Apple- king of all fruits have long been associated with the biblical story of Adam and Eve. " +
            "Between the Caspin and the Black Sea, the fruit was originated in the Middle East just about 4000 years ago!" +
            "It is one of the most favorite and popular fruits ever known. As with the well-known adage " +
            "'An apple a day keeps a doctor away' the fruit has been doing much good to people who are health conscious." +
            "In addition, even the fitness freaks prefer having this wonderful nutrient packed fruit." +
            "By all aspects, the fruit is indispensable. Apart from health care and nutrition, it is also " +
            "known for medicinal values. While the study of apples health benefits dates back to early stages," +
            "research to date suggests that its nutrients may play a role in promoting human health in a number of ways."
        },
        {
            "product": "Banana",
            "price": "$0.99",
            "image": "/static/assets/images/recommender/banana.jpeg",
            "description": "The banana is an edible fruit – botanically a berry[1 – produced by several kinds of large " +
            "herbaceous flowering plants in the genus Musa.[3] In some countries, bananas used for cooking may be" +
            "called plantains, in contrast to dessert bananas. The fruit is variable in size, color and firmness," +
            "but is usually elongated and curved, with soft flesh rich in starch covered with a rind which may be " +
            "green, yellow, red, purple, or brown when ripe. The fruits grow in clusters hanging from the top of " +
            "the plant. Almost all modern edible parthenocarpic (seedless) bananas come from two wild species – " +
            "Musa acuminata and Musa balbisiana. The scientific names of most cultivated bananas are Musa acuminata, " +
            "Musa balbisiana, and Musa × paradisiaca for the hybrid Musa acuminata × M. balbisiana, depending on " +
            "their genomic constitution. The old scientific name Musa sapientum is no longer used."
        },
        {
            "product": "Cherry",
            "price": "$1.49",
            "image": "/static/assets/images/recommender/cherry.jpg",
            "description": "A cherry is the fruit of many plants of the genus Prunus, and is a fleshy drupe (stone fruit)." +
            "The cherry fruits of commerce usually are obtained from a limited number of species such as cultivars " +
            "of the sweet cherry, Prunus avium. The name 'cherry' also refers to the cherry tree, and is sometimes " +
            "applied to almonds and visually similar flowering trees in the genus Prunus, as in 'ornamental cherry'" +
            "or 'cherry blossom'. Wild cherry may refer to any of the cherry species growing outside of cultivation, " +
            "although Prunus avium is often referred to specifically by the name 'wild cherry' in the British Isles."
        },
        {
            "product": "Peach",
            "price": "$2.50",
            "image": "/static/assets/images/recommender/peach.jpg",
            "description": "The peach (Prunus persica) is a deciduous tree native to the region of Northwest China between" +
            "the Tarim Basin and the north slopes of the Kunlun Shan mountains, where it was first domesticated " +
            "and cultivated. It bears an edible juicy fruit called a peach or a nectarine."
        },
        {
            "product": "Pomegranate",
            "price": "$3.69",
            "image": "/static/assets/images/recommender/pomegranate.jpg",
            "description": "The pomegranate, botanical name Punica granatum, is a fruit-bearing deciduous shrub or small tree in " +
            "the family Lythraceae that grows between 5 and 8 m (16 and 26 ft) tall.The fruit is typically in season " +
            "in the Northern Hemisphere from September to February, and in the Southern Hemisphere from March to May. " +
            "As intact arils or juice, pomegranates are used in baking, cooking, juice blends, meal garnishes, " +
            "smoothies, and alcoholic beverages, such as cocktails and wine."
        },
        {
            "product": "Avocado",
            "price": "$7.99",
            "image": "/static/assets/images/recommender/avocado.jpg",
            "description": "The avocado (Persea americana) is a tree that is native to South Central Mexico, " +
            "classified as a member of the flowering plant family Lauraceae.Avocado (also alligator pear) " +
            "also refers to the tree's fruit, which is botanically a large berry containing a single seed"
        },
        {
            "product": "Eggs",
            "price": "$5.15",
            "image": "/static/assets/images/recommender/eggs.jpg",
            "description": "Egg yolks and whole eggs store significant amounts of protein and choline,and " +
            "are widely used in cookery. Due to their protein content, the United States Department of " +
            "Agriculture categorizes eggs as Meats within the Food Guide Pyramid.Despite the nutritional " +
            "value of eggs, there are some potential health issues arising from egg quality, storage, and individual allergies."
        },
        {
            "product": "Coconut milk",
            "price": "$12",
            "image": "/static/assets/images/recommender/coconut_milk.png",
            "description": "Coconut milk is the liquid that comes from the grated meat of a mature coconut. " +
            "The opacity and rich taste of coconut milk are attributed to its high oil content, " +
            "most of which is saturated fat. Coconut milk is a popular food ingredient used in " +
            "Southeast Asia, the Caribbean, and northern South America."
        },
        {
            "product": "Soymilk",
            "price": "$6.33",
            "image": "/static/assets/images/recommender/soyMilk.jpg",
            "description": "Soy milk (also spelled soymilk) is a plant based drink produced by soaking dried soybeans " +
            "and grinding them in water.A traditional staple of East Asian cuisine, soy milk is a stable " +
            "emulsion of oil, water and protein. Soy milk can be produced at home using a soy milk machine. " +
            "It is often used as a substitute for dairy milk for individuals who are vegan or lactose intolerant"
        },
        {
            "product": "Almond milk",
            "price": "$7.25",
            "image": "/static/assets/images/recommender/milk_1.jpg",
            "description": "Almond milk is a plant milk manufactured from almonds with a creamy texture and nutty taste. " +
            "It contains neither cholesterol nor lactose, and is often consumed by those who are lactose-intolerant " +
            "and others who wish to avoid dairy products, including vegans. Commercial almond milk comes in " +
            "sweetened, unsweetened, plain, vanilla and chocolate flavors, and is usually enriched with vitamins. " +
            "It can also be made at home using a blender, almonds and water. It is traditionally consumed " +
            "through much of the Mediterranean"
        },
        {
            "product": "Butter unsalted",
            "price": "$15.99",
            "image": "/static/assets/images/recommender/unsalted_butter.png",
            "description": "Butter is a dairy product made by churning fresh or fermented cream or milk. In many parts " +
            "of the world, butter is an everyday food. Butter is used as a spread, as a condiment and in " +
            "cooking applications such as baking, sauce making, and frying. Butter consists of butterfat " +
            "surrounding minuscule droplets consisting mostly of water and milk proteins. The most common " +
            "form of butter is made from cows' milk, but butter can also be made from the milk of other mammals, " +
            "including sheep, goats, buffalo, and yaks. Salt, flavorings, or preservatives are sometimes " +
            "added to butter.Rendering butter produces clarified butter or ghee, which is almost entirely " +
            "butterfat. Unsalted butter is simply butter with no salt added. It is often used in baking. " +
            "Because there is no salt in it, it tends to spoil more quickly."
        },
        {
            "product": "Butter salted",
            "price": "$10.99",
            "image": "/static/assets/images/recommender/butter_salted.jpeg",
            "description": "Butter is a dairy product made by churning fresh or fermented cream or milk. In many parts " +
            "of the world, butter is an everyday food. Butter is used as a spread, as a condiment and in " +
            "cooking applications such as baking, sauce making, and frying. Butter consists of butterfat " +
            "surrounding minuscule droplets consisting mostly of water and milk proteins. The most common " +
            "form of butter is made from cows' milk, but butter can also be made from the milk of other mammals, " +
            "including sheep, goats, buffalo, and yaks. Salt, flavorings, or preservatives are sometimes " +
            "added to butter.Rendering butter produces clarified butter or ghee, which is almost entirely " +
            "butterfat.Traditionally, salt was added to butter as a preservative. Now salted butter is " +
            "considered the norm. "
        },
        {
            "product": "Salt",
            "price": "$8",
            "image": "/static/assets/images/recommender/salt.jpg",
            "description": "Salt is present in most foods, but in naturally occurring foodstuffs such as meats, " +
            "vegetables and fruit, it is present in very small quantities. It is often added to " +
            "processed foods (such as canned foods and especially salted foods, pickled foods, " +
            "and snack foods or other convenience foods), where it functions as both a " +
            "preservative and a flavoring. Dairy salt is used in the preparation of butter and " +
            "cheese products.[66] Before the advent of electrically powered refrigeration, " +
            "salting was one of the main methods of food preservation. Thus, herring contains 67 mg " +
            "sodium per 100 g, while kipper, its preserved form, contains 990 mg. Similarly, pork " +
            "typically contains 63 mg while bacon contains 1,480 mg, and potatoes contain 7 mg but " +
            "potato crisps 800 mg per 100 g.[12] The main sources of salt in the diet, apart from " +
            "direct use of sodium chloride, are bread and cereal products, meat products " +
            "and milk and dairy products"
        },
        {
            "product": "Green Tea",
            "price": "$7.15",
            "image": "/static/assets/images/recommender/green_tea.png",
            "description": "Green tea is a type of tea that is made from Camellia sinensis leaves that have " +
            "not undergone the same withering and oxidation process used to make oolong and " +
            "black tea. Green tea originated in China, but its production has spread to " +
            "many countries in Asia."
        },
        {
            "product": "Black Tea",
            "price": "$9.49",
            "image": "/static/assets/images/recommender/black_tea.jpg",
            "description": "Black tea is a type of tea that is more oxidized than oolong, green and white teas. " +
            "Black tea is generally stronger in flavor than the less oxidized teas. All four " +
            "types are made from leaves of the shrub (or small tree) Camellia sinensis. " +
            "Two principal varieties of the species are used – the small-leaved Chinese " +
            "variety plant (C. sinensis subsp. sinensis), used for most other types of teas, " +
            "and the large-leaved Assamese plant (C. sinensis subsp. assamica), which was " +
            "traditionally mainly used for black tea, although in recent years some green " +
            "and white have been produced."
        },
        {
            "product": "Coffee",
            "price": "$1.96",
            "image": "/static/assets/images/recommender/coffee.jpg",
            "description": "A coffee seed, commonly called coffee bean, is a seed of the coffee plant, and is the source for coffee. "
            + "It is the pit inside the red or purple fruit often referred to as a cherry. Just like ordinary cherries,"
            + " the coffee fruit is also a so-called stone fruit. Even though the coffee beans are seeds, they are referred "
            + "to as 'beans' because of their resemblance to true beans. The fruits – coffee cherries or coffee berries – "
            + "most commonly contain two stones with their flat sides together. A small percentage of cherries contain "
            + "a single seed, instead of the usual two. This is called a 'peaberry'. The peaberry occurs only between "
            + "10 and 15% of the time, and it is a fairly common (yet scientifically unproven) belief that they have more "
            + "flavour than normal coffee beans Like Brazil nuts (a seed) and white rice, coffee beans consist mostly of endosperm."
        },
        {
            "product": "White bread",
            "price": "$2.96",
            "image": "/static/assets/images/recommender/white_bread.jpg",
            "description": "White bread typically refers to breads made from wheat flour from which the bran and the germ "+
                            "layers have been removed (and set aside) from the whole wheatberry as part of the flour grinding "+
                            "or milling process, producing a light-colored flour. This milling process can give white flour a "+
                            "longer shelf life by removing the natural oils from the whole grain. Removing the oil allows "+
                            "products made with the flour, like white bread, to be stored for longer periods of time "+
                            "avoiding potential rancidity"
        },
        {
            "product": "Whole Wheat bread",
            "price": "$3.96",
            "image": "/static/assets/images/recommender/wheat_bread.jpg",
            "description": "Whole wheat bread or wholemeal bread is a type of bread made using flour that is partly or "+
                            "entirely milled from whole or almost-whole wheat grains, see whole-wheat flour and whole "+
                            "grain. It is one kind of brown bread. Synonyms or near-synonyms for whole-wheat bread outside "+
                            "the United States (e.g., the UK) are whole grain bread or wholemeal bread. Some varieties of "+
                            "whole-wheat bread are traditionally coated with whole or cracked grains of wheat, though this "+
                            "is mostly decorative compared to the nutritional value of a good quality loaf itself."
        }
    ];
    let isPresent = false;
    $(document).ready(function () {
         divolte.signal("ProductRecommendor_Search",{"queryString":searched.q});
        });
    $scope.products.forEach(function(element) 
    {
        if(searched.q == element.product)
            {
                isPresent = true;
                $scope.searched_product = element;
            }    
    }, this);
    if(isPresent)
    {
        let item = {};
        item['items'] = $scope.searched_product.product;
        $http.post(apiURL+"service/foodrecom",item).then(function(result)
        {
            $scope.recommended_products = [];
            let data = result.data.data;
            data.forEach(function(d)
            {
                $scope.products.forEach(function(element)
                {
                    if(d == element.product)
                    {
                        $scope.recommended_products.push(element);
                    }
                },this);

            },this);
        });
    }
});

