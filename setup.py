from distutils.core import setup


setup(name='enigma2-plugin-systemplugins-customsubservices',
		version='1.0',
		author='Dimitrij',
		author_email='dima-73@inbox.lv',
		package_dir={'SystemPlugins.CustomSubservices': 'src'},
		packages=['SystemPlugins.CustomSubservices'],
		package_data={'SystemPlugins.CustomSubservices': ['*.xml']},
		description='Switching subservices based on XML config'
	)
