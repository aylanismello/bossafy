import _ from 'lodash';
import React, { Component } from 'react';
import { Search, Grid, Header } from 'semantic-ui-react';

export default class MySearch extends Component {
	constructor(props) {
		super(props);
		this.handleResultSelect = this.handleResultSelect.bind(this);
		this.handleSearchChange = this.handleSearchChange.bind(this);
		this.state = {
			source: {}
		};
	}

	componentWillReceiveProps(nextProps) {
		if (!this.props.chords && nextProps.chords) {
			this.setState({
				source: Object.keys(nextProps.chords).map(chord => {
					return {
						title: chord
					};
				})
			});
		}
	}

	componentWillMount() {
		this.resetComponent();
	}

	resetComponent() {
		this.setState({ isLoading: false, results: [], value: '' });
	}

	handleResultSelect(e, { result }) {
		this.setState({ value: result.title });
    this.props.fetchNextChord(result.title);
	}

	handleSearchChange(e, { value }) {
		this.setState({ isLoading: true, value });

		setTimeout(() => {
			if (this.state.value.length < 1) return this.resetComponent();

			const re = new RegExp(_.escapeRegExp(this.state.value), 'i');
			const isMatch = result => re.test(result.title);

			this.setState({
				isLoading: false,
				results: _.filter(this.state.source, isMatch).slice(5)
			});
		}, 500);
	}

	render() {
		const { isLoading, value, results } = this.state;

		return (
			<Search
				loading={isLoading}
				onResultSelect={this.handleResultSelect}
				onSearchChange={this.handleSearchChange}
				results={results}
				value={value}
				{...this.props}
			/>
		);
	}
}
