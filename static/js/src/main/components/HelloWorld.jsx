import React from 'react';

export class HelloWorld extends React.Component {
	render(){
		return(
			<div>
			Hello {this.props.children}
			</div>
		)
	}
}
