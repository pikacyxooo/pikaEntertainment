rule = {
	max:'50',
	pattern:'^[a-zA-Z0-9]+\@[A-Za-z0-9]+\.(com|cn)$'
};
input_validate = new Validator('pikacyxooo@gmail.cm',rule);
// result = input_validate.validate_max();
result = input_validate.validate_reg();
console.log(result);