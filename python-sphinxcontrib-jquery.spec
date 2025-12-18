Name:		python-sphinxcontrib-jquery
Version:	4.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-jquery/sphinxcontrib-jquery-%{version}.tar.gz
Summary:	Extension to include jQuery on newer Sphinx releases
URL:		https://pypi.org/project/sphinxcontrib-jquery/
License:	GPL
Group:		Development/Python
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)


%description
Extension to include jQuery on newer Sphinx releases

%prep
%autosetup -p1 -n sphinxcontrib-jquery-%{version}

%files
%{py_sitedir}/sphinxcontrib/jquery
%{py_sitedir}/sphinxcontrib_jquery-*.*-info
