import _ from 'lodash';
import React, { Component } from 'react';
import { Search, Grid, Header } from 'semantic-ui-react';
const CHORD_TYPES = {
	NAME: 'NAME',
	TAB: 'TAB'
};

export default class MySearch extends Component {
	constructor(props) {
		super(props);
		this.handleResultSelect = this.handleResultSelect.bind(this);
		this.handleSearchChange = this.handleSearchChange.bind(this);
		this.state = {
			source: {},
			results: null,
			value: null,
			isLoading: false
		};
	}

	componentWillReceiveProps(nextProps) {
		if (nextProps.value !== this.props.value) {
			this.handleSearchChange(undefined, { value: nextProps.value });
		}

		if (
			(!this.props.chordDict && nextProps.chordDict) ||
			nextProps.chordType !== this.props.chordType
		) {
			this.setState({
				source: Object.keys(nextProps.chordDict).map(chord => {
					return {
						title: chord,
						description: nextProps.chordDict[chord]
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

	formatTab(tab) {
		return tab.split(' ').join('').toLowerCase();
	}

	viewSorting(before, after) {
		console.log('pre-sort');
		console.log(before);
		console.log('post-sort');
		console.log(after);
	}

	handleSearchChange(e, { value }) {
		this.setState({ isLoading: true, value });

		setTimeout(() => {
			if (this.state.value.length < 1) return this.resetComponent();

			const formattedValue = this.formatTab(this.state.value);
			// to check effectiveness of sorting, uncomment
			// this.viewSorting(_.filter(this.state.source, isMatch), this.getResults());

			this.setState({
				isLoading: false,
				results: this.getResults(formattedValue)
			});
		}, 500);
	}

	getResults(formattedValue = this.state.value) {
		const re = new RegExp(_.escapeRegExp(this.state.value), 'i');
		const isMatch = result => {
			return (
				re.test(result.title) || re.test(this.formatTab(result.description))
			);
		};

		return _.filter(this.state.source, isMatch)
			.sort(item => {
				if (
					item.title === formattedValue[0] ||
					item.description === formattedValue[0]
				) {
					return 1;
				} else {
					return -1;
				}
			})
			.slice(0, 5);
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
			/>
		);
	}
}
