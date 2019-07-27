test = {
  'name': 'q1c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sum(training_data.loc[:, 'in_rich_neighborhood'])
          191
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(training_data.loc[:, 'in_rich_neighborhood'].isnull())
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(add_in_rich_neighborhood(training_data, ['NAmes']).loc[:, 'in_rich_neighborhood'])
          299
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
