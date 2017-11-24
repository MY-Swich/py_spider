const Sequelize = require('sequelize');
const config = require('./config');

var sequelize = new Sequelize(config.database,config.username,config.password,{
    host:config.host,
    dialect: 'mysql',
    pool:{
        max:5,
        min:0,
        idle:30000
    }
});

var Pet = sequelize.define('pet',{
    id:{
        type: Sequelize.STRING(50),
        primaryKey:true
    },
    name:Sequelize.STRING(100),
    gender:Sequelize.BOOLEAN,
    birth:Sequelize.STRING(10),
    createdAt:Sequelize.BIGINT,
    updatedAt:Sequelize.BIGINT,
    version:Sequelize.BIGINT
},{
    timestamps:false
});

var now = Date.now();

Pet.create({
    id:'g-'+now,
    name:'Gaffey',
    gender:false,
    birth:'2017-07-07',
    createdAt:now,
    updatedAt:now,
    version:0
}).then(function(p){
    console.log('第一\n');
    console.log('created.'+JSON.stringify(p));
}).catch(function(err){
    console.log('failed: '+err);
});

(async()=>{
    var dog = await Pet.create({
        id:'d-'+now,
        name:'Odie',
        gender:false,
        birth:'2016-07-07',
        createdAt:now,
        updatedAt:now,
        version:0
    });
    console.log('created:'+JSON.stringify(dog));
    console.log('第2\n');
})();


(async () => {
    var pets = await Pet.findAll({
        where: {
            name: 'Gaffey'
        }
    });
    console.log('第3\n');
    console.log(`find ${pets.length} pets:`);
    for (let p of pets) {
        console.log(JSON.stringify(p));
        console.log('update pet...');
        p.gender = true;
        p.updatedAt = Date.now();
        p.version ++;
        await p.save();
        if (p.version === 3) {
            await p.destroy();
            console.log(`${p.name} was destroyed.`);
        }
    }
})();

// (async()=>{
//     var p =  await queryFromSomewhere();
//     p.gender = true;
//     p.updatedAt = Date.now();
//     p.version++;
//     await p.save();
// })();

// (async()=>{
//     var p = await queryFromSomewhere();
//     await p.destroy();
// })();