class Car{

    constructor(licence, driver){
        this.id;
        this.licence = licence;
        this.driver = driver;
        this.passenger;
    }

    printData(){
        console.log(`Car data. Licence: ${this.licence}, Driver: ${this.driver.name}, Document: ${this.driver.document}`);
    }
}
