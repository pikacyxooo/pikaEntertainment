window.Validator = function(val,rule) {
	this.validate_max = function(){
		val = parseFloat(val);
		return val <= rule.max;
	}
	this.validate_reg = function(){
		var reg = new RegExp(rule.pattern);
		return reg.test(val)
	}
}
