class Portfolio 
{
  constructor(fName, lName, age, bio) 
  {
    this._fName = fName;
    this._lName = lName;
    this._age = age;
    this._bio = bio;
  }

  // FULL NAME AND TO STRING 
  fullName() 
  {
    return this.fName + " " + this.lName;
  }

  toString() 
  {
    let result = "";
    result += "\nName: " + this.fullName();
    result += "\nAge: " + this.age;
    result += "\nBio: " + this.bio;
    return result;
  }


  // GET AND SET (get allows access while set changes the attribute)

  get fName() 
  {
    return this._fName;
  }

  set fName(newfName) 
  {
    this._fName = newfName;
  }

  get lName() {
    return this._lName;
  }

  set lName(newlName) {
    this._lName = newlName;
  }

  get age()
  {-
    return this._age;
  }

  set age(newAge)
  {
    this._age = newAge;
  }

  get bio()
  {
    return this._bio;
  }

  set bio(newBio)
  {
    this._bio = newBio;
  }
}

let bi = "To write a short bio you should first make an initial introduction introducing yourself in the first or first person. Your short bio should include your brand, your accomplishments, and your values and goals. Your short bio should be one to three short paragraphs or four to eight sentences long."

const johny = new Portfolio("John", "Doe", 5, bi);
console.log(johny.toString()); // Outputs: John Doe

johny.lName = "Dowey";
johny.bio = "lmao whatever that was";
console.log(johny.toString()); // Outputs: John Doe