class Account{

    constructor(name, document){
        this.id;
        this.name = name;
        this.document = document;
        this.email;
        this.password;
    }
    printData(){
        console.log(`Account Data. name:${this.name}, Account: ${this.document}`);
    }

}
