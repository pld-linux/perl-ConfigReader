%include	/usr/lib/rpm/macros.perl
%define	pdir	Config
%define	pnam	Reader
Summary:	ConfigReader -- Read directives from a configuration file
Summary(pl):	ConfigReader -- czytaj dyrektywy z pliku konfiguracyjnego
Name:		perl-ConfigReader
Version:	0.5
Release:	3
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ConfigReader is a set of classes for reading configuration files.
The programmer can easily specify the directives to be read, as well as
their default values and a parsing function or method to use.  A lot of
work went into error handling.

%description -l pl
ConfigReader jest zbiorem klas, s�u��cych do czytania plik�w
konfiguracyjnych.  Programista mo�e w prosty spos�b wskaza� dyrektywy do
przeczytania, ich domy�lne warto�ci i funkcj�, kt�r� nale�y zastosowa�
do sprawdzania sk�adni.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
touch Makefile.PL
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"ConfigReader::Spec");'
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_sitelib}/ConfigReader
%{perl_sitelib}/ConfigReader/*.pm
%{_mandir}/man3/*
